# Profile API with Cat Facts

A simple RESTful API built with Python/Flask that returns user profile information along with dynamic cat facts fetched from an external API.

## Features

- ✅ GET endpoint at `/me` returning JSON profile data
- 🐱 Dynamic cat facts from Cat Facts API
- ⏰ ISO 8601 formatted timestamps
- 🛡️ Comprehensive error handling
- 📝 Request logging
- 🌐 CORS enabled
- ❤️ Health check endpoint

## API Endpoint

### GET `/me`

Returns profile information with a random cat fact.

**Response Format:**
```json
{
  "status": "success",
  "user": {
    "email": "your@email.com",
    "name": "Your Name",
    "stack": "Python/Flask"
  },
  "timestamp": "2025-10-16T20:15:40.368Z",
  "fact": "Random cat fact here"
}
```

**Status Codes:**
- `200 OK` - Successful request
- `500 Internal Server Error` - Server error

### GET `/health`

Health check endpoint for monitoring.

**Response:**
```json
{
  "status": "healthy"
}
```

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git (for cloning the repository)

## Dependencies

The project uses the following Python packages:

- **Flask** (3.0.0) - Web framework
- **flask-cors** (4.0.0) - Cross-Origin Resource Sharing support
- **requests** (2.31.0) - HTTP library for API calls
- **python-dotenv** (1.0.0) - Environment variable management
- **gunicorn** (21.2.0) - WSGI HTTP server for production

All dependencies are listed in `requirements.txt`.

## Local Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/lawren-ai/dynamic_profile_endpoint
cd dynamic_profile_endpoint
```

### 2. Create a Virtual Environment

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the root directory:

```bash
touch .env
```

Add the following variables to your `.env` file:

```env
# User Profile Information (REQUIRED)
USER_EMAIL=your.email@example.com
USER_NAME=Your Full Name
USER_STACK=Python/Flask

# API Configuration (Optional - defaults provided)
CAT_FACTS_API_URL=https://catfact.ninja/fact
API_TIMEOUT=5

# Server Configuration (Optional - defaults provided)
PORT=5000
DEBUG=False
```


### 5. Run the Application

```bash
python app.py
```

The server will start at `http://localhost:5000`

### 6. Test the API

Open your browser or use curl:

```bash
curl http://localhost:5000/me
```

Or visit: `http://localhost:5000/me` in your browser.

## Environment Variables

### Required Variables

These variables **must** be set in your `.env` file:

| Variable | Description | Example |
|----------|-------------|---------|
| `USER_EMAIL` | Your email address | `john.doe@example.com` |
| `USER_NAME` | Your full name | `John Doe` |
| `USER_STACK` | Your backend technology stack | `Python/Flask` |

### Optional Variables

These variables have default values but can be customized:

| Variable | Description | Default |
|----------|-------------|---------|
| `CAT_FACTS_API_URL` | Cat Facts API endpoint | `https://catfact.ninja/fact` |
| `API_TIMEOUT` | External API timeout (seconds) | `5` |
| `PORT` | Server port number | `5000` |
| `DEBUG` | Enable Flask debug mode | `False` |

## Project Structure

```
.
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (create this)
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

## Deployment

### Deploy to Railway

1. Push your code to GitHub (ensure `.env` is in `.gitignore`)
2. Sign up at [Railway.app](https://railway.app)
3. Create a new project and connect your GitHub repository
4. Add environment variables in Railway dashboard
5. Deploy automatically!


## Error Handling

The API includes comprehensive error handling:

- **Network Timeouts:** Returns fallback message if Cat Facts API is slow
- **API Failures:** Graceful degradation with fallback messages
- **Missing Environment Variables:** Fails on startup with clear error message
- **404 Errors:** Returns JSON error response
- **500 Errors:** Logs error and returns generic error message

## Development

### Running in Debug Mode

Set `DEBUG=True` in your `.env` file:

```env
DEBUG=True
```

This enables:
- Auto-reload on code changes
- Detailed error messages
- Interactive debugger

**Note:** Never use debug mode in production!

### Logging

The application logs all requests and errors. Logs include:
- Timestamp
- Log level (INFO, ERROR)
- Message

View logs in the console where the application is running.

## Testing

Test the endpoints using curl:

```bash
# Test profile endpoint
curl http://localhost:5000/me

# Test health check
curl http://localhost:5000/health

# Test with formatted output
curl http://localhost:5000/me | python -m json.tool
```


## Troubleshooting

### Common Issues

**Issue:** `ModuleNotFoundError: No module named 'flask'`
- **Solution:** Install dependencies: `pip install -r requirements.txt`

**Issue:** `ValueError: Missing required environment variables`
- **Solution:** Create `.env` file and add required variables

**Issue:** `Port already in use`
- **Solution:** Change `PORT` in `.env` or stop the process using the port

**Issue:** Cat facts not loading
- **Solution:** Check your internet connection and API timeout settings

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -am 'Add feature'`
4. Push to branch: `git push origin feature-name`
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

**Name:** Ayotunde Akinboade  
**Email:** akinboadelawrenceayo@gmail.com  
**Stack:** Python/Flask

## Acknowledgments

- [Cat Facts API](https://catfact.ninja/) for providing cat facts
- Flask framework and community
- All contributors

---

Made with ❤️ and 🐱
