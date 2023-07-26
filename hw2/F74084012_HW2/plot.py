import matplotlib.pyplot as plt
import json

def plots(filename):
    f = open(filename)
    data = json.load(f)
    accuracy = [x for x in data]
    plt.plot(accuracy)
    plt.xlabel('epoch')
    plt.title(filename[:-5])
    # plt.show()
    plt.savefig(filename[0:-5]+".png")
    plt.clf()
    f.close()

plots("train_accuracy.json")
plots("train_loss.json")
plots("valid_accuracy.json")
plots("valid_loss.json")

