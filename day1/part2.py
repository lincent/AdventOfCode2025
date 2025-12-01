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
        
            [direction, stepCount] = decode_instruction(instruction.strip())

            totalRotations = stepCount // 100
            steps = stepCount % 100

            password += totalRotations
            startPosition = position

            if direction == LEFT:
                position = (position - steps) % 100
                if startPosition != 0 and steps >= startPosition:
                    password += 1
             
            if direction == RIGHT:
                position = (position + steps) % 100
                if startPosition != 0 and steps >= (100 - startPosition):
                    password += 1
    
    print(password)





