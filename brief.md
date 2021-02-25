# Brief

## Instructions
Your client is a clothing brand that is looking for a simple web app to use in their warehouses. To do their work efficiently, the warehouse workers need a fast and simple listing page per product category, where they can check simple product and availability information from a single UI. There are three product categories they are interested in for now: gloves, facemasks, and beanies. Therefore, you should implement three web pages corresponding to those categories that list all the products in a given category. One requirement is to be easily able to switch between product categories quickly. You are free to implement any UI you want, as long as it can display multiple products at once in a straightforward and explicit listing. At this point, it is not necessary to implement filtering or pagination functionality on the page.

The client does not have a ready-made API for this purpose. Instead, they have two different legacy APIs that combined can provide the needed information. The legacy APIs are on critical-maintenance-only mode, and thus further changes to them are not possible. The client knows the APIs are not excellent, but they are asking you to work around any issues in the APIs in your new application. The client has instructed you that both APIs have an internal cache of about 5 minutes.

### API documentation is as follows
`GET /v2/products/:category` – Return a listing of products in a given category.

`GET /v2/availability/:manufacturer`– Return a list of availability info.

The APIs are running at https://bad-api-assignment.reaktor.com/.

Your task is to implement a web application that fits the client brief and host the running solution somewhere where it can be accessed publicly (e.g. Heroku). Please include a link to the source code and the running application in your application.

###Some pointers you might want to take into account

You can keep the UI side simpler than it would be in a real-life situation. You do not need to implement filtering, search, or pagination.
Be mindful of page loading speed and error handling in the application code itself, but using free hosting options with long-ish startup times on the first load is fine.
The API is supposed to resemble working with a real-life legacy API. It has a built-in intentional failure case that you might run into while developing. To ease up reproducing the issue without needing to wait for the next random request failure, we provide a request header: x-force-error-mode. Set to all to force the failure to reproduce.
Have fun! 