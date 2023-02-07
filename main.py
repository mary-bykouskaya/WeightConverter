# Weight Converter
if __name__ == "__main__":
    # Enter weight in KG
    weight_kg = 999
    weight_pounds = 2000

    # Convert weight in KG to pouds (conv. voef. = 2.2)
    conv_coef = 2.12345
    weight_in_pounds = conv_coef * weight_kg
    weight_in_kg = weight_pounds / conv_coef
    weight_in_pounds = round(weight_in_pounds, 4)
    # Print result
    print(f"Weight {weight_kg} kg is equal to {weight_in_pounds:.2f} pounds")
    print(f"Weight {weight_pounds} pounds is equal to {weight_in_kg:.2f} kg")