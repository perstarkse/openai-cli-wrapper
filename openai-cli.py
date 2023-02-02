import openai
import click

savefile = open("log.json", "a")
openai.api_key = ""

@click.command()
@click.option('--temperature', default=0.7, help='Enter the temperature appropriate.')
@click.option('--prompt', prompt='Your prompt', help="The prompt to send to openai")
def search(temperature, prompt):
    result = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=2060,
        temperature=temperature
    )
    textResult = result['choices'][0]['text']
    print(textResult.strip('\n'))
    savefile.write(str(result))

if __name__ == '__main__':
    search()
