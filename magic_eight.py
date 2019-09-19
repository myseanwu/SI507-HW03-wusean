import random

def answer():
    while True:
        answer = input('What is your question?')
        reply = "As I see it, yes."
        reply2 = [ "It is certain.", "It is decidedly so." , "Without a doubt.","Yes - definitely.","You may rely on it.","As I see it, yes.",
               "Most likely.","Outlook good.", "Yes.","Signs point to yes.","Reply hazy, try again.","Ask again later.","Better not tell you now.",
                "Cannot predict now.","Concentrate and ask again.","Don't count on it.","My reply is no.","My sources say no.","Outlook not so good.","Very doubtful."]

        if answer == 'quit':
            break
        if not answer.endswith('?'):
            print("I'm sorry, I can only answer questions.")
        elif answer.endswith('?'):
            print(random.choice(reply2))
            break

if __name__ == '__main__':
    answer()
