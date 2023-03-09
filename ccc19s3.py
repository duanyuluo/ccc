# CCC '19 S3 - Arithmetic Square

def output(s, end = False, highlight=False, index=""):
    pass
# ************************ MUST REMOVE BEFORE SUMMIT ************************
from ccc import make_io
input, output = make_io(__file__, "tc2")
# ***************************************************************************

class Matrix():
    def __init__(self, row_list) -> None:
        self.row_list = row_list.copy()

    def __repr__(self):
        return "\n".join(repr(row) for row in self.rows())
    
    def __getitem__(self, row_index):
        return Sequence(Sequence.ROW, row_index, self)
    
    def __len__(self):
        return self.size_of()[0]
    
    def get_item(self, row_index, col_index):
        return self.row_list[row_index][col_index]
    
    def set_item(self, row_index, col_index, value):
        self.row_list[row_index][col_index] = value

    def size_of(self):
        return len(self.row_list), len(self.row_list[0])

    def copy(self):
        return Matrix(self.row_list)

    def rows(self):
        for idx, row in enumerate(self.row_list):
            yield Sequence(Sequence.ROW, idx, self)

    def columns(self):
        for idx in range(0, len(self.row_list[0])):
            yield Sequence(Sequence.COL, idx, self)
    
    def sequences(self):
        from itertools import chain
        for r in chain(self.rows(), self.columns()):
            yield r

class Sequence():
    ROW, COL = 0, 1

    def __init__(self, seq_type, idx, matrix) -> None:
        self.seq_type = seq_type
        self.index = idx
        self.matrix = matrix
        self.delta = None

    def __repr__(self) -> str:
        s = " ".join(["%2d" % v for v in self])
        return "<[%s[%s]]> " % (self.seq_type == Sequence.ROW and "R" or "C", self.is_valid() and "v" or "x") + s

    def __setitem__(self, idx, value):
        row, col = self.seq_type == Sequence.ROW and (self.index, idx) or (idx, self.index)
        self.matrix.row_list[row][col] = value

    def __getitem__(self, idx):
        row, col = self.seq_type == Sequence.ROW and (self.index, idx) or (idx, self.index)
        return self.matrix.row_list[row][col]
    
    def __len__(self):
        return self.matrix.size_of()[self.seq_type == Sequence.ROW and 1 or 0]
    
    def __iter__(self):
        self.cur = 0
        return self
    
    def __next__(self):
        try:
            row, col = self.seq_type == Sequence.ROW and (self.index, self.cur) or (self.cur, self.index)
            v = self.matrix[row][col]
            self.cur += 1
            return v
        except:
            raise StopIteration
    
    def unknowns(self):
        for i, v in enumerate(self):
            if v < 0:
                yield i, v

    def unknowns_cnt(self):
        return len([1 for (i, v) in self.unknowns()])
    
    def knowns(self):
        for i, v in enumerate(self):
            if v >= 0:
                yield i, v

    def knowns_cnt(self):
        return len(self) - self.unknowns_cnt()
    
    def __calc_delta(self):
        if self.knowns_cnt() >= 2:
            idx_list, value_list = tuple(zip(*[(i, v) for (i, v) in self.knowns()]))
            d = (value_list[1] - value_list[0]) / (idx_list[1] - idx_list[0])
            if d % 1 == 0:
                return int(d)
        return None
    
    def calc_sequence(self):
        if self.knowns_cnt() > 0 and self.delta != None:
            indexs, knowns = zip(*[(i, n) for (i, n) in enumerate(self) if n >= 0])
            sn = knowns[0] - indexs[0] * self.delta
            idxs, vals = zip(*[(i, n) for (i, n) in enumerate(self)])
            for i, n in zip(idxs, vals):
                if not i in indexs:
                    self[i] = sn + i * self.delta

    def validate(self, force_delta = None):
        if force_delta != None:
            self.delta = force_delta
        if self.delta == None:
            self.delta = self.__calc_delta()
        if self.delta != None:
            self.calc_sequence()

    def is_valid(self):
        return self.delta != None and \
            all([self[i] + self.delta == self[i+1] \
                 for i in range(0, len(self)-1)])
        
def calc_generator(start):
    yield start
    while True:
        start += 1
        yield start
        yield -start

matrix = Matrix([[p == "X" and -1 or int(p) \
                  for p in input().split(" ")] for i in range(0, 3)])

def validate_matrix(matrix, force_delta = None):
    last_valid_cnt = 0
    matrix_rows, matrix_cols = matrix.size_of() 
    while True:
        validations = []
        for seq in matrix.sequences():
            seq.validate(force_delta)
            force_delta = None
            if seq.is_valid():
                validations.append(seq)
            output(seq)

        if len(validations) == 0 or len(validations) == last_valid_cnt:
            return False
        elif len(validations) == matrix_rows + matrix_cols:
            return True
        else:
            last_valid_cnt = len(validations)

if not validate_matrix(matrix):
    for delta in calc_generator(0):
        try_matrix = matrix.copy()
        if validate_matrix(try_matrix, delta):
            output(try_matrix)
            matrix = try_matrix
            break

print(matrix)