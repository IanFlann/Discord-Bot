import random
from typing import Union, Tuple, Any

#import requests
import json


def handle_response(user_message, message) -> Union[str, tuple[str, Any]]:
    p_message = user_message.lower()

    if p_message == 'gatis':
        return 'Hey there!'

    if p_message == 'ur mother':
        return str(random.randint(1, 6))

    if p_message == "ponk":
        return "https://tenor.com/bWgRC.gif"

    if 'mommy' in p_message:
        return "In my talons, I shape clay, crafting life forms as I please. If I wish, I can smash it all. Around me is a burgeoning empire of steel. From my throne room, lines of power careen into the skies of Earth. My whims will become lightning bolts that raze the mounds of humanity. Out of the chaos, they will run and whimper, praying for me to end their tedious anarchy. I am drunk with this vision. God: the title suits me well."

    if 'trollt' in p_message:
        return "https://cdn.discordapp.com/attachments/751259365083709444/1031993137515728966/packet-tracer.png"