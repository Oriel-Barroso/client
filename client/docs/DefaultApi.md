# openapi_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user**](DefaultApi.md#create_user) | **POST** /api/v1/users/users | Create User
[**get_users**](DefaultApi.md#get_users) | **GET** /api/v1/users/users | Get Users


# **create_user**
> UserResponseSchema create_user(user_schema)

Create User

### Example


```python
import openapi_client
from openapi_client.models.user_response_schema import UserResponseSchema
from openapi_client.models.user_schema import UserSchema
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    user_schema = openapi_client.UserSchema() # UserSchema | 

    try:
        # Create User
        api_response = api_instance.create_user(user_schema)
        print("The response of DefaultApi->create_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_schema** | [**UserSchema**](UserSchema.md)|  | 

### Return type

[**UserResponseSchema**](UserResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users**
> List[UserResponseSchema] get_users()

Get Users

### Example


```python
import openapi_client
from openapi_client.models.user_response_schema import UserResponseSchema
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Get Users
        api_response = api_instance.get_users()
        print("The response of DefaultApi->get_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_users: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[UserResponseSchema]**](UserResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

