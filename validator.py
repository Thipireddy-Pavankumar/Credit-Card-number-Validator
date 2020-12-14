card_no = list(input("enter card no.").strip())
#check if no. of digits is 16
if len(card_no) == 16:
    #removing last digit
    check_bit = card_no.pop()
    #card_no = card_no[::-1]
    #reversed numbers as a list
    card_no.reverse()
    print(card_no)

    sum = 0

    for i in range(len(card_no)):
        #doubling numbers at even places
        if i%2 == 0:
            card_no[i] = int(card_no[i])*2
            #subtract 9 from numbers greater than 9
            if card_no[i]> 9:
                card_no[i] = card_no[i] - 9
        #sum of all the digits except check bit
        sum = sum+int(card_no[i])
    print(card_no)
    #adding check bit to the sum
    sum = sum + int(check_bit)
    print(sum)

    #the sum which is multiples of 10 is valid card
    if sum % 10 == 0:
        print("The Card is Valid")
    else:
        print("The card is Invalid!!!")
else:
    print("The card is Invalid!!!")

    
