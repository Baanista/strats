import numpy as np
import random
import copy


def create_nural(layers):
    conections = []
    # print('layers',len(layers))
    for i in range(len(layers) - 1):
        conections.append([])
        # print(layers[i+1])
        for a in range(layers[i + 1]):
            conections[i].append([])
            for j in range(layers[i]):
                # conections[i][a].append([0,0])
                conections[i][a].append([random.random() * 2 - 1, random.random() * 2 - 1])

    return conections

class Brain():
    
    def __init__(self, layers):
        self.net = create_nural(layers)

    # time.sleep(5)
    
    def plugin_info(self, data):
        layer = data
    
        node = []
    
        for _layer in range(len(self.net)):  # which node len(self.net)
            templayer = []
            # print(layer)
            for f in range(len(self.net[_layer])):
                for i in range((len(self.net[_layer][f]))):
                    # print(layer[i])
                    # print(self.net[_layer][f][i][1])
                    w1 = self.net[_layer][f][i][0]
                    w2 = self.net[_layer][f][i][1]
    
                    num = (w1 * layer[i]) + w2
                    # print(num)
                    node.append(num)
                    # print(node)
    
                if np.sum(node) >= 0:
                    # pri nt(node)
                    templayer.append(np.sum(node))
                else:
                    templayer.append(0)
    
                node = []
    
            layer = templayer
    
        # print(layer)
    
        return layer
    
    
    def scorer(self, input_data, output_data):
        outter = self.plugin_info(input_data)
    
        # print('out', outter)
    
        score = 0
    
        for i in range(len(outter)):
            score += abs((outter[i] - output_data[i]))
    
        return score
    
    
    def changer(self):
        for i in range(len(self.net)):
            for a in range(len(self.net[i])):
                for f in range(len(self.net[i][a])):
                    for two in range(2):
                        self.net[i][a][f][two] += (random.random() * 2 - 1)
    
        return self.net
    
    
    def trainer(self, input_all_data, output_all_data, batch_size):
        best_nural = self.net
    
        highest_score = 0
    
        for q in range(len(input_all_data)):
            highest_score += self.scorer(input_all_data[q], output_all_data[q])
    
        #print('bscore', highest_score)
        for a in range(batch_size):
            temp_score = 0
            temp_nural= self.changer(copy.deepcopy(self.net))
            for i in range(len(input_all_data)):
                temp_score += self.scorer(input_all_data[i], output_all_data[i])
            if highest_score > temp_score:
                highest_score = temp_score
                best_nural = temp_nural
                # print('changed', highest_score)
    
        return best_nural