def rename_selections(name_string: str, amount: int, start_number: int = 1) -> None:
    num_hash_chars = name_string.count("#")
    for i in range(amount):
        renamed_string = name_string.replace("#" * num_hash_chars, str(start_number).zfill(num_hash_chars))

        start_number += 1
        print(renamed_string)

rename_selections("Arm_###_Jnt", 7)
