# Error handling


# Chek age useing try and except

while True:
    try:
        age = int(input('What is your age? '))
        print(age - 3)
    except:
        print('Please enter a number')
    else:
        print('Thank you!')
        break


# Error handling 2


    def sum(num1, num2):
        try:
            return num1 / num2
        except (TypeError, ZeroDivisionError) as err:
            print(f'Please enter numbers {err}')
        except ZeroDivisionError as err:
            print(err)
        except:
            print('Unknown error')


# used a error handling used a try except


        def ag_count(age):
            try:
                age = int(input('What is your age? '))
                return age
            except ValueError:
                print('Please enter a number')
            else:
                print('Thank you!')
                break
