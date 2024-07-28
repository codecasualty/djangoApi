from rest_framework.views import APIView
from rest_framework.response import Response
# Response is standard response which django is expecting while calling our api
from rest_framework import status
# This helps us in creating apiview class on basis of apiview class
from rest_framework import viewsets
from profiles_api import serializers

# this if for request response of our code

class HelloApiView(APIView):
    """ test api view"""
    # need to pass self as caling object, request is something that we receive from django application,
     # so whenever we make get request this function will be called
    serializer_class = serializers.HelloSerializer
    def get(self, request , format= None):
        """return a list of apiview features"""
        an_apiview = [
        'uses http methods as functions (get , post , patch ,put ,delete)',
        'is similar to a traditional django view',
        'gives you the most control over your appications',
        'is mapped to url manually',
        ]

        # respnose object needs dict or list, to convert it to json
        return Response({'message' : 'Hello world' , 'an-apiview' : an_apiview})

        # serializer is feature form DRF which allows us to convert datainputs to python frameworks and viceversa
        # its kinda similar to djanog forms which will accept various datainputs
        # this will be helpfull for post and update api Methods

    def post(self , request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message' : message})
        else:
            return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk = None):
        # so here we update the complete object with particular primary key, here pk is none but that only mean we dont support primary key hereby
        return Response({'method','PUT'})

    def patch(self, request , pk = None):
        # this is for partial update , so now lets you just passed last_name, then it will update only lastname of given primary key entry
        # but in put if you passed only lastname it will completely remove the firstname of particular primary key entry
        return Response({'method' , 'PATCH'})

    def delete(self, request , pk = None):
        # this will delete the entry completely from databases
        return Response({'method' , 'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    serializer_class =  serializers.HelloSerializer
    def list(self, request):
        a_viewset = [
            'Uses actions like list , create, retrieve, update , partial_update',
            'Automatically maps to URLs using routers',
            'Provides more functionality with less code',

        ]

        return Response({'message' : 'Hello' , 'a_viewset' : a_viewset})

    def create(self , request):
        serializer  = serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message' : message})
        else:
            return Response (
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request , pk = None):
        return Response({'http_method' : 'GET'})

    def update(self , request , pk = None):
        return Response({'http_method': 'PUT'})

    def partial_update(self ,request , pk = None):
        return Response({'http_method' : 'PATCH'})

    def destroy(self , request , pk = None):
        return Response({'http_method': 'DELETE'})


"""
In the Django REST Framework (DRF), `APIView` and `Response` are both classes. Understanding the difference between classes and objects is crucial in
working effectively with Django and DRF. Here’s a brief explanation:

### Classes vs. Objects
- **Class**: A class is a blueprint for creating objects. It defines a set of attributes and methods that the instantiated objects will have. In your
 code, `APIView` and `Response` are examples of classes provided by DRF.
- **Object**: An object is an instance of a class. When you create an object from a class, you are creating an instance that has the characteristics
described by the class.

### `APIView`
`APIView` is a class in DRF that serves as the base class for all views in the framework when you are not using generic views. It provides the basic
 functionality for standard HTTP methods and ensures integration with other parts of the framework, like authentication and permission handling.

### `Response`
`Response` is a class in DRF that represents an HTTP response. Its main purpose is to return data that can easily be converted into various content
types, typically JSON, but it can handle other formats as well.

### `format=None` in the Code
The `format` parameter in your `get` method signature is a way to specify the output format of the response explicitly. It's optional and, if not
specified, DRF will determine the format based on the request's "Accept" header or the URL extension if you have configured URL suffix patterns.

#### Simple Example Explanation:
```python
class HelloApiView(APIView):


    def get(self, request, format=None):

        an_apiview = [
            'Uses HTTP methods as functions (GET, POST, PATCH, PUT, DELETE)',
            'Is similar to a traditional Django view',
            'Gives you the most control over your applications',
            'Is mapped to URLs manually',
        ]

        # Response object needs a dict or list to convert it to JSON
        return Response({'message': 'Hello world', 'an_apiview': an_apiview})
```

**What Happens Here?**
- When the `get` method of `HelloApiView` is invoked, it constructs a list of strings describing features of `APIView`.
- It then returns a `Response` object containing a dictionary. This dictionary is automatically rendered into a JSON format by DRF.
- The `format=None` allows this method to potentially handle different response formats, although by default, JSON is used.

This approach using `APIView` gives you detailed control over the processing of the request and the formation of the response, making it suitable for complex APIs that require custom business logic.


"""
"""
When a user visits the URL `http://127.0.0.1:8000/api/hello-view/`, the following sequence of events will occur based on your Django REST Framework (DRF) setup and the provided code:

1. **URL Routing**: The Django URL dispatcher will match the URL path `hello-view/` to the configured route in your `urlpatterns`.
This route is linked to the `HelloApiView` class through the `as_view()` method, which DRF uses to create an instance of the view.

2. **View Processing**:
   - The `HelloApiView` class inherits from `APIView`, which provides methods for handling various HTTP methods. In your case, the `get` method is defined.
   - When the URL is accessed with a GET request, the `get` method on the `HelloApiView` instance is invoked.
   - Django's request handling mechanism automatically passes the `request` object to the `get` method. The `format` parameter is
   also passed, which defaults to `None` if not specified in the URL or headers.

3. **Generating a Response**:
   - Inside the `get` method, a list of strings describing the API view is created. This list highlights that the view:
     - Uses HTTP methods as function calls (e.g., GET, POST, PATCH, PUT, DELETE).
     - Is similar to traditional Django views but is specifically tailored for APIs.
     - Provides extensive control over application behavior.
     - Must be explicitly mapped to URLs.
   - A `Response` object is then created and returned. This object takes a dictionary as an argument. The dictionary includes a
   welcoming message and the list of API view features.
   - The `Response` class handles converting this dictionary into a JSON format. DRF includes content negotiation to determine
   the best renderer to use based on the `Accept` header in the request or the `format` query parameter.


4. **Sending the Response**:
   - The server sends the JSON response back to the client. By default, the response will include a 200 OK status unless specified otherwise.
   - The JSON body of the response will look like this:
     ```json
     {
         "message": "Hello world",
         "an-apiview": [
             "uses http methods as functions (get, post, patch, put, delete)",
             "is similar to a traditional django view",
             "gives you the most control over your applications",
             "is mapped to url manually"
         ]
     }
     ```

5. **Client-side Rendering**:
   - The browser or any client making the request will receive this JSON data and can process or render it as needed.

By visiting the specified URL, the user effectively triggers this sequence, leading to a clear demonstration of how DRF handles API
requests and produces structured responses suitable for integration with frontend technologies or other clients expecting JSON data.



The line `serializer_class = serializers.HelloSerializer` defines a class variable that references the `HelloSerializer` class from the `serializers` module.
This class is likely a custom serializer defined to handle data validation and serialization for specific data, such as a `name` field in your example.

Here’s a breakdown of the rest of the code and your questions:

### What is `serializer` here?

In the given method `post`, `serializer` is an instance of `HelloSerializer`. This instance is created by passing `request.data` to the serializer. `request.data`
contains the data submitted in the HTTP POST request. The serializer instance is then responsible for converting this data into Python data types, validating it against
the serializer's fields, and preparing it for further processing or saving to the database.

### Does `serializer` have inbuilt methods `isValid()` and `validated_data.get()`?

Yes, in Django's REST Framework:

- **`isValid()`**: This should actually be `is_valid()`. It's a method used to validate the data. It checks whether the data provided to the serializer adheres to
the rules specified in the serializer (like field requirements, data types, etc.). It returns `True` if the data is valid, otherwise `False`.

- **`validated_data`**: This is an attribute, not a method, that contains the data that was deemed valid after calling `is_valid()`. This data is then accessible
in a dictionary-like format.

- **`validated_data.get('name')`**: This method retrieves the `name` value from the validated data if it exists, otherwise it returns `None` (or another default
value if specified).

### What does `validated_data` mean?

`validated_data` is a dictionary-like attribute of the serializer instance that stores the clean and validated data. This data is safe to use for further processing
or saving to a database because it conforms to the validation rules defined in the serializer. After you call `is_valid()`, this attribute is populated with the data that passed validation checks.

### Corrected Code Explanation

```python
def post(self, request):
    serializer = self.serializer_class(data=request.data)  # Create an instance of the serializer with incoming request data
    if serializer.is_valid():  # Validate the data
        name = serializer.validated_data.get('name')  # Retrieve the 'name' field from validated data if validation passed
        message = f'Hello {name}'
        return Response({'message': message})
    else:
        return Response(
            serializer.errors,  # Return any errors encountered during validation
            status=status.HTTP_400_BAD_REQUEST  # Use HTTP 400 instead of 404 for client-side input errors
        )
```
Here, the method checks if the data is valid using `is_valid()` and uses the clean, validated data if it is. If the data isn’t valid, it returns the errors encountered
during validation. Note the change from `HTTP_404_BAD_REQUEST` to `HTTP_400_BAD_REQUEST` as 400 is more appropriate for data validation errors.


### What is a ViewSet?

A `ViewSet` in Django REST Framework (DRF) is a class that provides the functionality of a set of similar views, and is used for handling common
CRUD (Create, Read, Update, Delete) operations in a more organized way. It abstracts the logic of the standard actions that can be performed on a particular model.
This can make the code more concise and easier to maintain, especially for simple CRUD interfaces.

### How does it work?

`ViewSet` classes don't provide any method handlers such as `.get()` or `.post()` for specific HTTP methods. Instead, they provide actions such as
`.list()`, `.create()`, `.retrieve()`, `.update()`, and `.partial_update()`, which correspond to standard HTTP methods:
- `list()`: GET requests to retrieve a list of objects.
- `create()`: POST requests to create new objects.
- `retrieve()`: GET requests to retrieve a single object by an ID.
- `update()`: PUT requests to update an object completely.
- `partial_update()`: PATCH requests to update parts of an object.
- `destroy()`: DELETE requests to delete an object.

These actions are automatically routed when using routers provided by DRF, which automatically set up the URLs associated with the viewset actions.

### Differences Between ViewSets and APIViews

- **Routing**:
  - `APIView` requires explicit mapping of HTTP methods to class methods in your URL configuration. For each different type of request (GET, POST, etc.),
   you must define how it is handled in your views.py file.
  - `ViewSet` automatically sets up URL routes using DRF’s routers. A router checks the incoming request method and routes it to the appropriate action in
  the viewset, significantly simplifying URL configuration.

- **Code Simplicity**:
  - With `APIView`, you typically have to write more method-specific code to handle different HTTP requests. This includes defining separate classes or
   methods for different CRUD operations on the same resource.
  - `ViewSet` combines the logic of dealing with common data patterns into a single class where different operations are handled by different
  well-defined actions, reducing the amount of code you need to write.

- **Use Case**:
  - `APIView` is suitable when you need to perform custom processing and have more control over the logic, or when your API doesn’t neatly fit into the
  standard CRUD operations.
  - `ViewSet` is ideal for straightforward CRUD interfaces on a database model and when you want to reduce the amount of boilerplate code you write for
  an API that adheres closely to standard database operations.



"""
