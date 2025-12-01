LEFT = "Left"
RIGHT = "Right"

def decode_instruction(instruction):
    direction = LEFT if instruction[0] == 'L' else RIGHT
    stepCount = int(instruction[1:])

    print(f"{direction}:{stepCount}")

    return [direction, stepCount]

if __name__ == "__main__":

    position = 50
    password = 0
    
    with open("input.txt") as instructions:
        for instruction in instructions:
        
            [direction, stepCount] = decode_instruction(instruction)

            steps = stepCount % 100

            if direction == LEFT:
                position = (position - steps) % 100
             
            if direction == RIGHT:
                position = (position + steps) % 100
    
            print(f"New Position: {position}")
            if position == 0:
                password += 1
    
    print(password)





