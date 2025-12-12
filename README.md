# Recommendation System for E-Learning Platform


## Overview

This repository contains a Python-based recommendation system designed for an e-learning fullstack application. The primary function of this system is to recommend authors (users) using a graph data structure, optimizing user engagement and network building within the platform.  
Recommendations are dynamically generated based on MongoDB data, ensuring that author details and their connections are always up-to-date.

> **Integrated with:**  
Tech-Community-App[(E-Learning Fullstack App)](https://github.com/YUGESHKARAN/Node-Blog-App.git)

---

## Features

- **Graph-Based Recommendations:**  
  Utilizes graph data structures to model and analyze user relationships for accurate follower recommendations.

- **Live MongoDB Integration:**  
  Author and connection data are fetched in real-time from MongoDB, ensuring recommendations reflect the current state of the e-learning platform.

- **Python Implementation:**  
  Core recommendation logic and supporting scripts are written in Python for efficiency and flexibility.

- **Easy Integration:**  
  Designed to be modular and easily integrated into Node.js/Express-based e-learning applications.

- **Template Support:**  
  Includes template files for web-based interaction.

---

## Directory Structure

| File/Folder       | Description                                                   |
|-------------------|---------------------------------------------------------------|
| `index.py`        | Main entry point for running the recommendation engine        |
| `rcmd.py`         | Core recommendation logic leveraging graph data structures    |
| `schema.py`       | Defines data schemas and MongoDB data fetching logic          |
| `requirements.txt`| Lists Python dependencies                                     |
| `templates/`      | Contains HTML templates for web UI                            |
| `vercel.json`     | Deployment configuration for Vercel                           |
| `__pycache__/`    | Python bytecode cache (auto-generated)                        |

---

## How It Works

The recommendation system models users and their connections as a graph. By analyzing the structure of the graph, it identifies and suggests new followers for a user, aiming to enhance their learning network.

**MongoDB Integration:**  
- The system fetches author details (email and following list) directly from MongoDB using the logic in `schema.py`.
- This ensures recommendations are always based on the latest data.

**Key Implementation in `schema.py`:**
```python
def get_recommendation_dict():
    recommendation_dict = {}
    
    # Fetch only email and followers fields
    authors = authors_collection.find({}, {"email": 1, "following": 1, "_id": 0})

    for author in authors:
        recommendation_dict[author["email"]] = author.get("following", [])  # Default to empty list if no followers

    return recommendation_dict
```
- This function returns a dictionary where each author's email is mapped to a set of their connections (users they follow).

**Main Steps:**
1. **Data Modeling:**  
   Users and their relationships are represented as nodes and edges in a graph, sourced from MongoDB.
2. **Recommendation Algorithm:**  
   The system traverses the graph to find relevant users to recommend based on existing connections and other criteria.
3. **Integration:**  
   The system exposes endpoints or functions that can be called from the main e-learning app to fetch recommendations.

---

## Getting Started

### Prerequisites

- Python 3.7+
- MongoDB database with author data (email and following fields)
- (Recommended) Virtual environment tool: `venv` or `virtualenv`

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YUGESHKARAN/recommendation-system.git
   cd recommendation-system
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure MongoDB Connection:**
   - Update the MongoDB URI and collection details in `schema.py` as needed.

### Running the System

```bash
python index.py
```

- Access the web interface (if applicable) via the local server as indicated in the console output.

---

## Deployment

- The repository includes a `vercel.json` file for deployment on [Vercel](https://vercel.com/).
- For other deployment options (Heroku, AWS, etc.), ensure you adjust configuration as needed.

---

## Integration Guide

To integrate with your main e-learning app (Node-Blog-App):

- Use HTTP endpoints, shared database access, or API calls as per your architecture.
- Refer to the `index.py` and `rcmd.py` files for available functions and endpoints.
- The recommendation data is always live and reflects the current state of the MongoDB database.

---

## Contributing

Contributions are welcome! Open issues or pull requests for feature additions, bug fixes, or suggestions.

---

## License

This project is licensed under the MIT License.

---

## Acknowledgments

- Special thanks to the open-source community for graph algorithm inspirations.

---

*For questions or support, Open an issue in this repository.*
