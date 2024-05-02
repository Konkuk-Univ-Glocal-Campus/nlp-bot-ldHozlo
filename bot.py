import random

# This list contains the random responses (you can add your own or translate them into your own language too)
random_responses = ["흥미롭네요, 자세히 말씀해 주세요.",
                    "그렇군요. 계속하세요.",
                    "왜 그런 말을 합니까?",
                    "요즘 날씨가 참 재미있네요, 그렇죠?",
                    "주제를 바꿔 봅시다.",
                    "어젯밤 경기는 보셨나요?"]

print("안녕하세요, 저는 간단한 로봇 마빈입니다.")
print("'안녕'를 입력하면 언제든지 대화를 종료할 수 있습니다.")
print("각 답을 입력한 후 '엔터'를 눌러주세요")
print("\n\n오늘 어때요?")

while True:
    # wait for the user to enter some text
    user_input = input("> ")
    if user_input.lower() == "안녕":
        # if they typed in 'bye' (or even BYE, ByE, byE etc.), break out of the loop
        break
    else:
        response = random.choices(random_responses)[0]
    print(response)

print ("이야기해서 좋았어, 안녕!")
