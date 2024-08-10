import random
import string
def repeatCode():
    print(
        "Specify Complexity:\n 1. Only Letters\n 2. Only Digits\n 3. Only Special Characters\n 4. Letters+Digits\n 5. Letters+Special Characters\n 6. Digits+Special Characters\n 7. All Types Combined");
    pick = int(input())

    if (pick <= 7):

        if (pick == 1):
            characters_set = string.ascii_letters

        elif (pick == 2):
            characters_set = string.digits;

        elif (pick == 3):
            characters_set = string.punctuation;

        elif (pick == 4):
            characters_set = string.ascii_letters + string.digits;

        elif (pick == 5):
            characters_set = string.ascii_letters + string.punctuation;

        elif (pick == 6):
            characters_set = string.digits + string.punctuation;

        elif (pick == 7):
            characters_set = string.ascii_letters + string.digits + string.punctuation;

        def pass_generator(len):
            password = "".join(random.choices(characters_set, k=len));
            return password;

        print("Desired Password: " + pass_generator(len));


    else:
        print("Invalid choice. Try Again!");
        repeatCode();


characters_set = "";
password = [];

print("Enter the length of the password:");
len = int(input());
repeatCode();
