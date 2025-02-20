# Schema
petstore_api.paths.fake.get.request_body.content.application_x_www_form_urlencoded.schema
```
type: schemas.Schema
```

## validate method
Input Type | Return Type | Notes
------------ | ------------- | -------------
[SchemaDictInput](#schemadictinput), [SchemaDict](#schemadict) | [SchemaDict](#schemadict) |

## SchemaDictInput
```
type: typing.Mapping[str, schemas.INPUT_TYPES_ALL]
```
Key | Type |  Description | Notes
------------ | ------------- | ------------- | -------------
**enum_form_string_array** | [EnumFormStringArrayTupleInput](#enumformstringarraytupleinput), [EnumFormStringArrayTuple](#enumformstringarraytuple) | Form parameter enum test (string array) | [optional]
**enum_form_string** | typing.Literal["_abc", "-efg", "(xyz)"] | Form parameter enum test (string) | [optional] must be one of ["_abc", "-efg", "(xyz)"] if omitted the server will use the default value of -efg
**any_string_name** | dict, schemas.immutabledict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.FileIO | any string name can be used but the value must be the correct type | [optional]

## SchemaDict
```
base class: schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]

```
### &lowbar;&lowbar;new&lowbar;&lowbar; method
Keyword Argument | Type | Description | Notes
---------------- | ---- | ----------- | -----
**enum_form_string_array** | [EnumFormStringArrayTupleInput](#enumformstringarraytupleinput), [EnumFormStringArrayTuple](#enumformstringarraytuple), schemas.Unset | Form parameter enum test (string array) | [optional]
**enum_form_string** | typing.Literal["_abc", "-efg", "(xyz)"], schemas.Unset | Form parameter enum test (string) | [optional] must be one of ["_abc", "-efg", "(xyz)"] if omitted the server will use the default value of -efg
**kwargs** | schemas.immutabledict, tuple, float, int, str, bool, None, bytes, schemas.FileIO | any string name can be used but the value must be the correct type | [optional] typed value is accessed with the get_additional_property_ method

### properties
Property | Type | Description | Notes
-------- | ---- | ----------- | -----
**enum_form_string_array** | [EnumFormStringArrayTuple](#enumformstringarraytuple), schemas.Unset | Form parameter enum test (string array) | [optional]
**enum_form_string** | typing.Literal["_abc", "-efg", "(xyz)"], schemas.Unset | Form parameter enum test (string) | [optional] must be one of ["_abc", "-efg", "(xyz)"] if omitted the server will use the default value of -efg

### methods
Method | Input Type | Return Type | Notes
------ | ---------- | ----------- | ------
from_dict_ | [SchemaDictInput](#schemadictinput), [SchemaDict](#schemadict) | [SchemaDict](#schemadict) | a constructor
get_additional_property_ | str | schemas.immutabledict, tuple, float, int, str, bool, None, bytes, schemas.FileIO, schemas.Unset | provides type safety for additional properties

# EnumFormStringArray
```
type: schemas.Schema
```

## Description
Form parameter enum test (string array)

## validate method
Input Type | Return Type | Notes
------------ | ------------- | -------------
[EnumFormStringArrayTupleInput](#enumformstringarraytupleinput), [EnumFormStringArrayTuple](#enumformstringarraytuple) | [EnumFormStringArrayTuple](#enumformstringarraytuple) |

## EnumFormStringArrayTupleInput
```
type: typing.Union[
    typing.List[
        typing.Literal[
            ">",
            "$"
        ],
    ],
    typing.Tuple[
        typing.Literal[
            ">",
            "$"
        ],
        ...
    ]
]
```
List/Tuple Item Type | Description | Notes
-------------------- | ------------- | -------------
typing.Literal[">", "$"] |  | must be one of [">", "$"] if omitted the server will use the default value of $

## EnumFormStringArrayTuple
```
base class: typing.Tuple[
    typing.Literal[">", "$"],
    ...
]
```
### &lowbar;&lowbar;new&lowbar;&lowbar; method
Argument | Type
-------- | ------
arg      | [EnumFormStringArrayTupleInput](#enumformstringarraytupleinput), [EnumFormStringArrayTuple](#enumformstringarraytuple)
configuration | typing.Optional[schema_configuration.SchemaConfiguration] = None

### methods
Method | Input Type | Return Type | Notes
------ | ---------- | ----------- | ------
&lowbar;&lowbar;getitem&lowbar;&lowbar; | int | typing.Literal[">", "$"] | must be one of [">", "$"] if omitted the server will use the default value of $ This method is used under the hood when instance[0] is called
