import yaz

from .log import logger


class {{cookiecutter.app_name}}(yaz.BasePlugin):
    @yaz.task
    async def hello_world(self, greeting: str = 'Hello World!', shout: bool = False):
        if shout:
            greeting = greeting.upper()
        logger.debug('Sending greeting')
        return greeting
