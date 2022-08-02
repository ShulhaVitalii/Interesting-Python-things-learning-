class FileAcceptor:
    def __init__(self, *args):
        self.files = [*args]

    def __call__(self, filename, *args, **kwargs):
        return True if filename.split('.')[-1] in self.files else False

    def __add__(self, other):
        files = (i for i in set(self.files + other.files))
        return FileAcceptor(*files)


filenames = ["boat.jpg", "ans.web.png", "text.txt", "www.python.doc", "my.ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.xls", "ff.mp3"]
acceptor_images = FileAcceptor("jpg", "jpeg", "png")
acceptor_docs = FileAcceptor("txt", "doc", "xls")
filenames = list(filter(acceptor_images + acceptor_docs, filenames))

print(filenames)

