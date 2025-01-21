# My Own HTTP Server

## credentials:
- user: admin
- password: ginni26

An HTTP server built from scratch using **Python**, **HTML**, **CSS**, and **JavaScript** that supports `GET` and `POST` methods. This project is designed to understand the fundamentals of web servers and how they handle client requests and responses.

## Features

- **Custom HTTP Server**: Handles `GET` and `POST` requests.
- **Static File Serving**: Serves HTML, CSS, and JavaScript files.
- **Dynamic Response Handling**: Processes `POST` requests and returns appropriate responses.
- **Lightweight and Simple**: No external libraries required beyond Python's standard library.

## Requirements

- **Python 3.8+**

## How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/my-own-http-server.git
   cd my-own-http-server
   ```

2. Run the server:
   ```bash
   python server.py
   ```

3. Open your browser and navigate to:
   ```
   http://<your-ip-address>:2626
   ```

## Server Endpoints

### `GET /`
- Serves the `index.html` file.

### `POST /submit`
- Processes form data submitted via the `POST` method.
- Returns a dynamically generated response using `response.html`.

## Example Usage

### Submitting a Form
1. Open the home page at `http://<your-ip-address>:2626`.
2. Fill out the form and submit it.
3. The server processes the data and displays a confirmation page.

## Customization

- **HTML/CSS/JS**: Modify the files to change the front-end.
- **Dynamic Responses**: Update the `login.html and index.html` template to customize server responses.

## Learning Objectives

- Understand the HTTP protocol and how servers process requests.
- Learn to handle `GET` and `POST` methods programmatically.
- Gain insights into serving static and dynamic content.

## Future Enhancements

- Add support for more HTTP methods like `PUT` and `DELETE`.
- Implement a logging system for requests and responses.
- Include error handling for unsupported routes or methods.

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue to suggest improvements or report bugs.

---

Happy coding! 🚀
![Screenshot (74)](https://github.com/user-attachments/assets/2455450f-f87a-4322-9074-74f3b08850db)
![Screenshot (75)](https://github.com/user-attachments/assets/1ae77e5e-5b31-45d8-9eff-a9f4af677f72)


