import hashlib

def crack_password(hash_to_crack, password_file):
    # Read the file with potential passwords
    with open(password_file, 'r') as file:
        for password in file:
            # Remove any trailing newline characters
            password = password.strip()
            
            # Hash the password using SHA-256
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            
            # Check if the hash matches the hash_to_crack
            if hashed_password == hash_to_crack:
                print(f'Password found: {password}')
                return password
        
    print('Password not found')
    return None

# Example usage
if __name__ == '__main__':
    # Replace with your own hash and password file path
    hash_to_crack = '5e884898da28047151d0e56f8dc6292773603d0d4115e3f0c848b7f5e9fa1a11'  # Example hash (SHA-256 of 'password')
    password_file = 'passwords.txt'  # Path to a file containing a list of common passwords
    
    crack_password(hash_to_crack, password_file)
