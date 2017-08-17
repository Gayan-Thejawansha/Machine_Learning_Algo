from sklearn.datasets import load_iris
from sklearn import tree
import pydotplus
from PIL import Image as img
from IPython.display import Image

iris = load_iris ()
clf = tree.DecisionTreeClassifier ()
clf = clf.fit(iris.data , iris.target)
print clf.predict ([[4,1,6 ,1]])


dot_data = tree.export_graphviz (clf , out_file =None)
graph = pydotplus.graph_from_dot_data(dot_data)
print graph
#graph.write_pdf("iris.pdf")



dot_data = tree.export_graphviz (clf,out_file =None ,
feature_names =iris.feature_names ,
class_names =iris.target_names ,
filled=True , rounded=True ,
special_characters =True)
graph = pydotplus.graph_from_dot_data(dot_data)
#Image(graph.create_png())
#graph.write_png("iris.png")


image = img.open("iris.png")
image.show ()


print clf.predict(iris.data [:1, :])
print clf.predict_proba (iris.data [:1, :])