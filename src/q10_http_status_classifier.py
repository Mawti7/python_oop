# HTTP Exercise: Status Code Classifier
# Demonstrates HTTP status code classification

def classify_status(code: int) -> str:
    if 200 <= code <= 299:
        if code == 201:
            return "Created"
        else:
            return "Success"
    elif 400 <= code <= 499:
        return "Client Error"
    elif 500 <= code <= 599:
        return "Server Error"
    else:
        return "Other"

if __name__ == "__main__":
    codes = [200, 201, 400, 401, 403, 404, 500, 502, 503]
    for c in codes:
        print(c, "->", classify_status(c))
