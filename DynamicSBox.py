def main():
    int_list = [
    13, 11,  1, 12,  1, 10,  0, 11, 13,  7, 10,  9,  5,  6,  3,  6,
    9,  0, 14, 11,  5, 10,  3,  0, 14,  2,  6,  2, 15,  8,  1, 13,
    1,  3,  5,  0, 14,  7,  8,  9,  7, 13,  2,  2, 14,  4,  4, 13,
    15,  7, 12, 14,  4,  6,  2, 15, 12,  8,  8,  7, 10,  3,  4, 15
    ]
    binary_list = integers_to_binary(int_list)

    raw_bits = "Eric-Jacob Daley"
    bit_string = ''.join(format(ord(char), '08b') for char in raw_bits)
    modified_string = encrypt_round(bit_string, binary_list)
    for i in range(15):
        modified_string = encrypt_round(modified_string, binary_list)

    # Convert each character in raw_bits to its 8-bit binary representation
    print("Original:", bit_string)
    print("Modified:", modified_string)

def integers_to_binary(int_list):
    binary_list = [format(num, '04b') for num in int_list]
    return binary_list

def encrypt_round(bit_string, binary_list):
    xored_string = interate_bits(bit_string)
    modified_string = substitution_bits(xored_string, binary_list)
    return modified_string

def interate_bits(bit_string):
    result = []
    reps = len(bit_string)//2
    for i in range(reps):
        bit1 = bit_string[i]
        bit2 = bit_string[i+reps]
        bit1 = int(bit1, 2)
        bit2 = int(bit2, 2)
        xored = bit1^bit2
        result.append(str(xored))
    if len(bit_string)%2 == 1:
        result.append(bit_string[-1])
    end_bits = bit_string + ''.join(result)
    return end_bits

def substitution_bits(bit_string, binary_list):
    result = []
    # Process the string in chunks of 6 bits
    for i in range(0, len(bit_string) // 6 * 6, 6):
        chunk = bit_string[i:i+6]
        # Convert to list for mutability
        chunk_list = list(chunk)
        inner_bits = ''.join(chunk_list[0] + chunk_list[-1])
        outer_bits = ''.join(chunk_list[1:5])
        inner_bits = int(inner_bits, 2)
        outer_bits = int(outer_bits, 2)
        sBox_index = inner_bits*8 + outer_bits
        # Append the modified chunk to the result
        result.append(''.join(binary_list[sBox_index]))
    
    # Append the remaining unmodified bits, if any
    remaining_bits = len(bit_string) % 6
    if remaining_bits:
        result.append(bit_string[-remaining_bits:])
    
    return ''.join(result)

if __name__ == '__main__':
    main()