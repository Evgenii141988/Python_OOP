class Layer:
    def __init__(self):
        self.next_layer = None
        self.name = 'Layer'

    def __call__(self, obj: object):
        self.next_layer = obj
        return obj


class Input(Layer):
    def __init__(self, inputs: int):
        super().__init__()
        self.name = 'Input'
        self.inputs = inputs


class Dense(Layer):
    def __init__(self, inputs: int, outputs: int, activation: str):
        super().__init__()
        self.name = 'Dense'
        self.inputs = inputs
        self.outputs = outputs
        self.activation = activation


class NetworkIterator:
    def __init__(self, network: object):
        self.network = network

    def __iter__(self):
        while self.network:
            yield self.network
            self.network = self.network.next_layer



if __name__ == '__main__':
    network = Input(128)
    layer = network(Dense(network.inputs, 1024, 'linear'))
    layer = layer(Dense(layer.inputs, 10, 'softmax'))
    for x in NetworkIterator(network):
        print(x.name)
