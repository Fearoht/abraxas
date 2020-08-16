import os
import sys
import pickle
import random
import hashlib

class DataReader:

    def _disk_saving_pkl(self, dataframe, filename="", folder=""):
        path = os.getcwd()
        try:
            if os.path.isdir(path + "/" + folder) == False:
                os.mkdir(path + "/" + folder)
        except OSError:
            pass
        else:
            filename = hashlib.md5(filename.encode())
            filename = path + "/" + folder + "/" + filename.hexdigest()
            output = open(filename + '.pkl', 'wb')
            pickle.dump(dataframe, output)
            output.close()

    def _disk_loading_pkl(self, filename="", folder=""):
        path = os.getcwd()
        filename = hashlib.md5(filename.encode())
        filename = path + "/" + folder + "/" + filename.hexdigest()
        try:
            input = open(filename + '.pkl', 'rb')
        except OSError:
            return False, pd.DataFrame()
        else:
            df = pickle.load(input)
            input.close()
            return True, df

    def _disk_saving_csv(self, dataframe, filename="", folder=""):
        path = os.getcwd()
        try:
            if os.path.isdir(path + "/" + folder) == False:
                os.mkdir(path + "/" + folder)
        except OSError:
            pass
        else:
            dataframe.to_csv(path + "/" + folder + "/" + filename + ".csv")

    def _disk_loading_csv(self, filename="", folder="", index="Target"):
        path = os.getcwd()
        filename = path + "/" + folder + "/" + filename
        try:
            input = open(filename + '.csv', 'r')
        except OSError:
            return False, pd.DataFrame()
        else:
            df = pd.read_csv(filename+".csv")
            df = df.set_index(index)
            return True, df

    def _disk_loading_csv_online(self, filename="", folder="", index="Target"):
        df = pd.read_csv(filename)
        df = df.set_index(index)
        return True, df

    def _disk_saving_data(self, dataframe, filename="", folder=""):
        path = os.getcwd()
        try:
            if os.path.isdir(path + "/" + folder) == False:
                os.mkdir(path + "/" + folder)
        except OSError:
            pass
        else:
            cols = ""
            dimensions = 0
            for col in dataframe.columns:
                cols = cols + col + ";"
                dimensions = dimensions + 1
            cols = cols.strip(';')

            f = open(path + "/" + folder + "/" + filename + ".data", "w")
            f.write("DY\n")
            f.write(str(len(dataframe.index)) + "\n")
            f.write(str(dimensions) + "\n")
            f.write(cols + "\n")

            id = 1
            for idx, row in dataframe.iterrows():
                line = str(id) + ";"
                for feat in dataframe.columns:
                    if row[feat] is None or math.isnan(row[feat]):
                        row[feat] = 0
                    line = line + str(row[feat]) + ";"
                line = line  + str(idx)
                f.write(line + "\n")
                id = id + 1
            f.close()

    def _disk_loading_data(self, filename="", folder="", index="Target"):
        path = os.getcwd()
        filename = path + "/" + folder + "/" + filename
        try:
            file = open(filename + '.data', 'r')
        except OSError:
            return False, pd.DataFrame()
        else:
            file.readline()
            rows = int(file.readline())
            cols = int(file.readline())
            columns = file.readline().rstrip().split(";")
            columns.append(index)
            dots = []
            for r in range(0,rows):
                line = file.readline().rstrip().split(";")
                dot = []
                for c in range(1,cols+1):
                    dot.append(float(line[c]))
                dot.append(line[cols+1] if (len(columns) - len(line) == 1) else "NN")
                dots.append(dot)
            df = pd.DataFrame(dots,columns=columns)
            df = df.set_index(index)
            return True, df

    def __init__(self, file="",index="Target", format="pkl"):
        file_path = file
        path = ""
        file = file.split("/")
        if len(file) == 1:
            file,ext = file[0].split(".")
        else:
            path = file_path
            file,ext = file[len(file)-1].split(".")

        valid_file = False
        self.df = pd.DataFrame()
        if format == "pkl":
            valid_file, self.df = self._disk_loading_pkl(filename=file, folder="datasets")
        elif format == "csv":
            valid_file, self.df = self._disk_loading_csv(filename=file, folder="csv", index=index)
        elif format == "data":
            valid_file, self.df = self._disk_loading_data(filename=file, folder="data", index=index)
        
        if not valid_file:
            if ext == "csv":
                if path != "":
                    valid_file, self.df = self._disk_loading_csv_online(filename=path, folder="", index=index)
                else:    
                    valid_file, self.df = self._disk_loading_csv(filename=file, folder="", index=index)
            elif ext == "data":
                valid_file, self.df = self._disk_loading_data(filename=file, folder="", index=index)
            self._disk_saving_pkl(
                dataframe = self.df,
                filename = file, folder="datasets")
            self._disk_saving_csv(
                dataframe = self.df,
                filename = file, folder="csv")
            self._disk_saving_data(
                dataframe = self.df,
                filename = file, folder="data")

    def gather(self):
        return self.df.copy()
