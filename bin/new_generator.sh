#!/usr/bin/env bash

set -euo pipefail
set -o noclobber

usage() {
cat <<EOF
Stubs out files for new generators

Usage:
$0 [options]
    Options:
$(grep "[[:space:]].)\ #" $0 | tr -d "#" | sed -E 's/( \| \*)//' | sed -E 's/([a-zA-Z])\)/-\1/')

Examples:
  Create a server generator for ktor:
  $0 -n kotlin -s

    Creates:
    src/main/java/org/openapijsonschematools/codegen/generators/KotlinServerCodegen.java
    src/main/resources/kotlin-server/README.mustache
    src/main/resources/kotlin-server/model.mustache
    src/main/resources/kotlin-server/api.mustache
    bin/configs/kotlin-server-petstore-new.yaml

  Create a generic C# server generator:
  $0 -n csharp -s -t
    Creates:
    src/main/java/org/openapijsonschematools/codegen/generators/CsharpServerCodegen.java
    src/main/resources/csharp-server/README.mustache
    src/main/resources/csharp-server/model.mustache
    src/main/resources/csharp-server/api.mustache
    bin/configs/csharp-server-petstore-new.yaml
    src/test/java/org/openapijsonschematools/codegen/csharp/CsharpServerCodegenTest.java
    src/test/java/org/openapijsonschematools/codegen/csharp/CsharpServerCodegenModelTest.java
    src/test/java/org/openapijsonschematools/codegen/csharp/CsharpServerCodegenOptionsTest.java
    src/test/java/org/openapijsonschematools/codegen/options/CsharpServerCodegenOptionsProvider.java
EOF
    exit 0;
}

declare os=${OSTYPE//[0-9.]/}
declare root=$(cd $(dirname "${BASH_SOURCE}") && pwd)
declare gen_type=
declare tests=0
declare gen_name

checkPreviousGenType() {
    if [ "a" != "a$gen_type" ]; then
        echo "[error] You may only set a single generator type at a time!" >&2
        usage >&2
        exit 1
    fi
}

[ $# -eq 0 ] && usage
while getopts ":hcsdtfHn:" arg; do
  case ${arg} in
    n) # Required. Specify generator name, should be kebab-cased.
      gen_name=${OPTARG}
      ;;
    c) # Create a client generator
        checkPreviousGenType
        gen_type=client
        ;;
    s) # Create a server generator
        checkPreviousGenType
        gen_type=server
        ;;
    d) # Create a documentation generator
        checkPreviousGenType
        gen_type=documentation
        ;;
    H) # Create a schema generator
        checkPreviousGenType
        gen_type=schema
        ;;
    f) # Create a config generator
        checkPreviousGenType
        gen_type=config
        ;;
    t) # When specified, creates test file(s) for the generator.
      tests=1
      ;;
    h | *) # Display help.
      usage
      exit 0
      ;;
  esac
done

if [ -z "$gen_type" ]; then
    echo "[error] You may set a generator type" >&2
    usage >&2
    exit 1
fi

[ -z "${gen_name}" ] && usage

titleCase() {
  if [ "$os" == "darwin" ]; then
    echo $1 | tr '-' ' ' | tr '_' ' ' | ruby -e "print STDIN.gets.split.map(&:capitalize).join(' ')" | tr -d ' '
  else
    read -ra words <<< $(echo $1 | tr '-' ' ' | tr '_' ' ')
    echo "${words[@]^}" | tr -d ' '
  fi
}

kebabCase() {
  echo $1 | tr '_' ' ' | tr ' ' '-' | tr '[:upper:]' '[:lower:]'
}

kebabCasePath() {
  echo $1 | tr '_' ' ' | tr ' ' '-' | tr '-' '/' | tr '[:upper:]' '[:lower:]'
}

kebabCasePathWin() {
  echo $1 | tr '_' ' ' | tr ' ' '-' | tr '-' '\\' | tr '[:upper:]' '[:lower:]'
}

kebabCasePkg() {
  echo $1 | tr '_' ' ' | tr ' ' '-' | tr '-' '.' | tr '[:upper:]' '[:lower:]'
}

upperCase() {
  echo $1 | tr '[[:lower:]]' '[[:upper:]]'
}

declare lang_classname=$(titleCase "${gen_name}-${gen_type}-Codegen")
declare gen_name_camel=$(kebabCase "${gen_name}")
declare gen_name_camel_path=$(kebabCasePath "${gen_name}")
declare gen_name_camel_pathwin=$(kebabCasePathWin "${gen_name}")
declare gen_name_camel_pkg=$(kebabCasePkg "${gen_name}")
declare codegen_type_enum=$(upperCase "${gen_type}")

# Step 1: Add Language Generator
[ -f "${root}/src/main/java/org/openapijsonschematools/codegen/generators/${lang_classname}.java" ] && \
    echo "${lang_classname} already exists" && exit 1;

echo "Creating src/main/java/org/openapijsonschematools/codegen/generators/${lang_classname}.java"
cat > "${root}/src/main/java/org/openapijsonschematools/codegen/generators/${lang_classname}.java" <<EOF
package org.openapijsonschematools.codegen.generators;

import org.openapijsonschematools.codegen.*;
import io.swagger.models.properties.ArrayProperty;
import io.swagger.models.properties.MapProperty;
import io.swagger.models.properties.Property;
import io.swagger.models.parameters.Parameter;

import java.io.File;
import java.util.*;

import org.apache.commons.lang3.StringUtils;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class ${lang_classname} extends DefaultCodegen implements CodegenConfig {
    public static final String PROJECT_NAME = "projectName";

    static final Logger LOGGER = LoggerFactory.getLogger(${lang_classname}.class);

    public CodegenType getTag() {
        return CodegenType.${codegen_type_enum};
    }

    public String getName() {
        return "${gen_name_camel}";
    }

    public String getHelp() {
        return "Generates a ${gen_name_camel} ${gen_type}.";
    }

    public ${lang_classname}() {
        super();

        outputFolder = "generated-code" + File.separator + "${gen_name_camel}";
        modelTemplateFiles.put("model.mustache", ".zz");
        apiTemplateFiles.put("api.mustache", ".zz");
        embeddedTemplateDir = templateDir = "${gen_name_camel}";
        apiPackage = "Apis";
        modelPackage = "Models";
        supportingFiles.add(new SupportingFile("README.mustache", "", "README.md"));
        // TODO: Fill this out.
    }
}
EOF

# Step 2: Register the new class with service loader
echo -e "\norg.openapijsonschematools.codegen.generators.${lang_classname}" >> "${root}/src/main/resources/META-INF/services/org.openapijsonschematools.codegen.generators.Generator"

# Step 3: Create resource files
mkdir -p "${root}/src/main/resources/${gen_name_camel}"
echo "Creating src/main/resources/${gen_name_camel}/README.mustache" && \
    touch "${root}/src/main/resources/${gen_name_camel}/README.mustache"
echo "Creating src/main/resources/${gen_name_camel}/model.mustache" && \
    touch "${root}/src/main/resources/${gen_name_camel}/model.mustache"
echo "Creating src/main/resources/${gen_name_camel}/api.mustache" && \
    touch "${root}/src/main/resources/${gen_name_camel}/api.mustache"

# Step 4: Create generation config scripts
echo "Creating bin/configs/${gen_name_camel}-petstore-new.yaml"
cat > "${root}/bin/configs/${gen_name_camel}-petstore-new.yaml"<<EOF
generatorName: ${gen_name_camel}
outputDir: samples/${gen_type}/petstore/${gen_name_camel_path}
inputSpec: src/test/resources/3_0/petstore.yaml
templateDir: src/main/resources/${gen_name_camel}
additionalProperties:
  hideGenerationTimestamp: "true"
EOF

# Step 5: (optional) Create OpenAPI Generator test files
if [ "1" -eq "${tests}" ]; then
    mkdir -p "${root}/src/test/java/org/openapijsonschematools/codegen/${gen_name_camel_path}"
    # Codegen
    echo "Creating src/test/java/org/openapijsonschematools/codegen/generators/${lang_classname}Test.java"
    cat > "${root}/src/test/java/org/openapijsonschematools/codegen/generators/${lang_classname}Test.java"<<EOF
package org.openapijsonschematools.codegen.${gen_name_camel_pkg};

import org.openapijsonschematools.codegen.*;
import org.openapijsonschematools.codegen.generators.${lang_classname};
import io.swagger.models.*;
import io.swagger.parser.SwaggerParser;
import org.testng.Assert;
import org.testng.annotations.Test;

public class ${lang_classname}Test {

    ${lang_classname} codegen = new ${lang_classname}();

    @Test
    public void shouldSucceed() throws Exception {
        // TODO: Complete this test.
        Assert.fail("Not implemented.");
    }
}
EOF

    # Options
    echo "Creating src/test/java/org/openapijsonschematools/codegen/generators/options/${lang_classname}OptionsTest.java"
    cat > "${root}/src/test/java/org/openapijsonschematools/codegen/generators/options/${lang_classname}OptionsTest.java"<<EOF
package org.openapijsonschematools.codegen.${gen_name_camel_pkg};

import org.openapijsonschematools.codegen.AbstractOptionsTest;
import org.openapijsonschematools.codegen.CodegenConfig;
import org.openapijsonschematools.codegen.generators.${lang_classname};
import org.openapijsonschematools.codegen.options.${lang_classname}OptionsProvider;

import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.verify;

public class ${lang_classname}OptionsTest extends AbstractOptionsTest {
    private ${lang_classname} codegen = mock(${lang_classname}.class, mockSettings);

    public ${lang_classname}OptionsTest() {
        super(new ${lang_classname}OptionsProvider());
    }

    @Override
    protected CodegenConfig getCodegenConfig() {
        return codegen;
    }

    @SuppressWarnings("unused")
    @Override
    protected void verifyOptions() {
        // TODO: Complete options using Mockito
        // verify(codegen).someMethod(arguments)
    }
}

EOF

    # Options Provider
    echo "Creating src/test/java/org/openapijsonschematools/codegen/generators/options/${lang_classname}OptionsProvider.java"
    cat > "${root}/src/test/java/org/openapijsonschematools/codegen/generators/options/${lang_classname}OptionsProvider.java"<<EOF
package org.openapijsonschematools.codegen.options;

import org.openapijsonschematools.codegen.CodegenConstants;
import org.openapijsonschematools.codegen.generators.${lang_classname};

import com.google.common.collect.ImmutableMap;

import java.util.Map;

public class ${lang_classname}OptionsProvider implements OptionsProvider {
    public static final String PROJECT_NAME_VALUE = "OpenAPI";

    @Override
    public String getLanguage() {
        return "${gen_name_camel}";
    }

    @Override
    public Map<String, String> createOptions() {
        ImmutableMap.Builder<String, String> builder = new ImmutableMap.Builder<String, String>();
        return builder
                .put(${lang_classname}.PROJECT_NAME, PROJECT_NAME_VALUE)
                .build();
    }

    @Override
    public boolean isServer() {
        return false;
    }
}

EOF
fi

echo "Finished."
