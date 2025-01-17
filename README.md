# Verify_IP - Is the IP from Brazil?

This repository contains a Python script designed to verify whether a given IP address belongs to Brazil. It uses the public API from **ipinfo.io** to gather information about the IP address and determine its country of origin.

## How It Works

The script sends a request to the **ipinfo.io** API with the provided IP address. The API returns detailed information about the IP, including its country. If the country code returned is **BR**, the script confirms that the IP belongs to Brazil.

### Features

- Verifies if a given IP address is from Brazil.
- Uses the public API **ipinfo.io**.
- Provides clear and simple output for the user.
- Handles connection errors gracefully.

## Requirements

Before running the script, ensure you have Python installed along with the following library:

```bash
pip install requests
```

## Usage

1. Clone this repository:

   ```bash
   git clone https://github.com/hrpeter/verify_IP.git
   ```

2. Navigate to the project directory:

   ```bash
   cd verify_IP
   ```

3. Run the script:

   ```bash
   python verify_IP.py
   ```

4. Enter the IP address when prompted, and the script will tell you whether the IP belongs to Brazil or not.

### Example

```bash
Digite o endereço IP para verificar: 187.94.52.102
O IP 187.94.52.102 pertence ao Brasil.
```

## Contributing

Feel free to open issues or submit pull requests if you would like to contribute to this project.

## License

This project is licensed under the MIT License.
