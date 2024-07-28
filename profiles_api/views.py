from rest_framework.views import APIView
from rest_framework.response import Response
# Response is standard response which django is expecting while calling our api

# This helps us in creating apiview class on basis of apiview class
class HelloApiView(APIView):
    """ test api view"""
    # need to pass self as caling object, request is something that we receive from django application,
     # so whenever we make get request this function will be called

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
"""
