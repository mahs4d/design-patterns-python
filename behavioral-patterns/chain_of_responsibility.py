from abc import ABC, abstractmethod


class RequestHandler(ABC):
    @abstractmethod
    def on_request(self, request, next_handler):
        pass


class RequestChain:
    def __init__(self):
        self._chain = []

    def add_handler(self, handler):
        self._chain.append(handler)
        return self

    def on_request(self, request):
        if len(self._chain) == 0:
            return None

        next_handler = self._generate_next_function(request, 0)
        return next_handler()

    def _generate_next_function(self, request, i):
        def next_handler(passed_request=None):
            if len(self._chain) <= i:
                return None

            if passed_request is None:
                return self._chain[i].on_request(request, self._generate_next_function(request, i + 1))

            return self._chain[i].on_request(request, self._generate_next_function(passed_request, i + 1))

        return next_handler


# region usage


class LoggerRequestHandler(RequestHandler):
    def on_request(self, request, next_handler):
        response = next_handler()
        print(f'request: {request}, response: {response}')
        return response


class IncrementRequestHandler(RequestHandler):
    def on_request(self, request, next_handler):
        incremented_request = request + 1
        next_handler()
        return incremented_request


if __name__ == '__main__':
    chain = RequestChain()
    chain.add_handler(LoggerRequestHandler()).add_handler(IncrementRequestHandler())
    result = chain.on_request(1)
    print(f'final result: {result}')

# endregion
