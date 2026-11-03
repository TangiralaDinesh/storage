import binascii

def main():
    print("--- Built-in CRC-32 Generator & Verifier ---")
    
    # 1. Input message from user
    message = input("Enter a text message to send: ").strip()
    message_bytes = message.encode("utf-8")
    
    # --- SENDER SIDE ---
    # Generate the 32-bit CRC checksum
    checksum = binascii.crc32(message_bytes)
    print(f"\n[ Sender ]")
    print(f"Original Message: '{message}'")
    print(f"Generated CRC-32: {checksum} (Hex: {hex(checksum)})")
    
    # --- RECEIVER SIDE ---
    print("\n[ Receiver ]")
    received_message = input("Enter received text (press Enter to simulate no errors): ").strip()
    
    # If the user presses enter, assume no transmission error occurred
    if not received_message:
        received_message = message
        
    received_bytes = received_message.encode("utf-8")
    
    # Verify the received message by checking its CRC against the sender's CRC
    receiver_checksum = binascii.crc32(received_bytes)
    
    print(f"Received CRC-32:  {receiver_checksum} (Hex: {hex(receiver_checksum)})")
    
    if checksum == receiver_checksum:
        print("Result: Success! CRCs match. No errors detected.")
    else:
        print("Result: Error! CRCs mismatch. The data was corrupted!")

if __name__ == "__main__":
    main()
