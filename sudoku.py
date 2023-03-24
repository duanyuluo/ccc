
def output(s, end = False, highlight=False, index=""):
    pass
# ************************ MUST REMOVE BEFORE SUMMIT ************************
from ccc import make_io
input, output = make_io(__file__, "tc6")
# ***************************************************************************

from copy import deepcopy
from itertools import combinations

class SudokuException(Exception):
    def __init__(self, cell, sequence, msg) -> None:
        super().__init__(cell, sequence, msg)
        self.cell = cell
        self.seq = sequence
        self.msg = msg

from collections.abc import Iterable, Iterator
class MatrixIterator(Iterator):
    def __init__(self, iter_obj) -> None:
        super().__init__()
        self.index = 0
        self.iter_obj = iter_obj

    def __next__(self):
        if self.index >= len(self.iter_obj):
            raise StopIteration
        value = self.iter_obj[self.index]
        self.index += 1
        return value


class Cell():
    def __init__(self, r, c, m) -> None:
        self.row_index, self.col_index = r, c
        self.matrix = m

    def __str__(self) -> str:
        v = self.get_value()
        return self.is_exactly() and ("%2d" % v) or ("?%1d" % len(v))

    def __repr__(self) -> str:
        return "(%d, %d) %s" % (self.row_index, self.col_index, self.get_value())

    def get_value(self):
        v = self.matrix.data[self.row_index][self.col_index]
        return (v == 0 and (Matrix.NUMBERS, 0) or (v, 0))[0]

    def set_value(self, value):
        if type(value) == set and len(value) == 1:
            self.matrix.data[self.row_index][self.col_index] = value.copy().pop()
        else:
            self.matrix.data[self.row_index][self.col_index] = type(value) == set and value.copy() or value

    def is_exactly(self):
        v = self.get_value()
        return type(v) == int

class Sequence():
    ROW, COLUMN, BLOCK, TIP = "R", "C", "B", "T"

    def __init__(self, seq_type, index, matrix) -> None:
        self.seq_type = seq_type
        self.index = index
        self.matrix = matrix
        self.cur = 0

    def __len__(self):
        if self.seq_type == Sequence.TIP:
            return len(self.matrix.tips_seq[self.matrix.tips_name[self.index]])
        return self.matrix.size

    def __str__(self) -> str:
        return " ".join([str(c) for (i, c) in enumerate(self)])

    def __repr__(self) -> str:
        return "[%s] #%d : %s" % (self.seq_type, self.index, " ".join([str(c) for (i, c) in enumerate(self)]))

    def __iter__(self):
        return MatrixIterator(self)

    def __next__(self):
        if self.cur >= self.matrix.size:
            raise StopIteration
        elif self.seq_type == Sequence.TIP and self.cur >= len(self.matrix.tips_seq[self.tips_name[self.index]]):
            raise StopIteration
        v = self[self.cur]
        self.cur += 1
        return v

    def __get_position(self, index):
        if self.seq_type == Sequence.ROW:
            return self.index, index
        elif self.seq_type == Sequence.COLUMN:
            return index, self.index
        elif self.seq_type == Sequence.BLOCK:
            block_row = (self.index // 3) * 3 + (index // 3)
            block_col = (self.index % 3) * 3 + (index % 3)
            return block_row, block_col
        elif self.seq_type == Sequence.TIP:
            tip_mark = self.matrix.tips_name[self.index]
            return self.matrix.tips_seq[tip_mark][index]

    def __getitem__(self, index):
        row, col = self.__get_position(index)
        return Cell(row, col, self.matrix)

    def __setitem__(self, index, value):
        row, col = self.__get_position(index)
        Cell(row, col, self.matrix).set_value(value)

    def superset_cells(self, superset):
        for cell in self:
            cell_options = cell.get_value()
            if cell.is_exactly():
                cell_options = set([cell_options, ])
            if cell_options <= superset:
                yield cell, set()
            elif cell_options & superset:
                yield cell, cell_options - superset

class Matrix():
    NUMBERS = {i for i in range(1, 10)}

    def __init__(self, data, tips_data = [], tips_nums = {}) -> None:
        self.data = deepcopy(data)
        self.tips_data = tips_data
        self.tips_num = tips_nums
        self.tips_seq = {}
        self.tips_name = [n for n in tips_nums.keys()]
        self.size = len(self.data)
        self.__range_tip_seqs__()

    def __range_tip_seqs__(self):
        for row in range(0, self.size):
            for col in range(0, self.size):
                if self.tips_data[row][col] == 0:
                    continue
                if not self.tips_data[row][col] in self.tips_seq:
                    self.tips_seq[self.tips_data[row][col]] = []
                self.tips_seq[self.tips_data[row][col]].append((row, col))

    def __str__(self) -> str:
        return "\n".join([str(row) for (i, row) in enumerate(self.rows())])

    def __repr__(self) -> str:
        return "\n".join([repr(c) for c in self.cells()])

    def copy(self):
        return Matrix(self.data, self.tips_data, self.tips_num)

    def __getitem__(self, index):
        return Sequence(Sequence.ROW, index, self)

    def rows(self):
        return [Sequence(Sequence.ROW, i, self) for i in range(0, self.size)]

    def columns(self):
        return [Sequence(Sequence.COLUMN, i, self) for i in range(0, self.size)]

    def blocks(self):
        return [Sequence(Sequence.BLOCK, i, self) for i in range(0, self.size)]

    def tips(self):
        return [Sequence(Sequence.TIP, i, self) for i in range(0, len(self.tips_name))]

    def sequences(self):
        from itertools import chain
        return chain(self.rows(), self.columns(), self.blocks(), self.tips())

    def cells(self):
        for row in self.rows():
            for cell in row:
                yield cell

    def output(self):
        cell_fmt = lambda c: c.is_exactly() and str(c) or ("<{%2s}>" % str(c))
        leader = lambda i: (i // 3) in [0, 2] and "<[ ]>" or " "
        output("<[         ]>         <[         ]>\n")
        for i, row in enumerate(self.rows()):
            row_str = " ".join([cell_fmt(c) for c in row])
            output(row_str + leader(i))

class Guessture():
    def __init__(self, matrix, row, col, guessture) -> None:
        self.guess_matrix = matrix.copy()
        self.backup_matrix = matrix
        self.row_index = row
        self.col_index = col
        self.guess_matrix[self.row_index][self.col_index] = guessture
        self.guessture = guessture

    def __repr__(self) -> str:
        return "(%d, %d) %s" % (self.row_index, self.col_index, self.guessture)

    def replace_matrix(self, matrix):
        return self.guess_matrix

    def rollback_matrix(self):
        return self.backup_matrix

    @staticmethod
    def make_cell_guesstures(cell):
        return [Guessture(cell.matrix, cell.row_index, cell.col_index, guess) \
                for guess in cell.get_value()]

class Resolver():
    def __init__(self, matrix) -> None:
        self.counters = {"Resolve Cycles": 0, "Sequence Rules": 0, "Guess Times": 0}
        self.matrix = matrix
        self.sequence_rules = []
        self.blocker_rules = []
        self.guess_rules = []
        self.guesstures = []
        self.histories = []

    def resolve_once(self):
        modified = False
        for seq in self.matrix.sequences():
            for rule in self.sequence_rules:
                self.counters["Sequence Rules"] += 1
                if rule(seq):
                    modified = True
        return modified

    def resolve_until(self):
        output("RESOLVE #%d..." % self.counters["Resolve Cycles"], highlight=True)
        self.matrix.output()
        while self.resolve_once():
            self.histories.append(self.matrix.copy())
            cs = [c for c in self.matrix.cells() if not c.is_exactly()]
            if len(cs) == 0:
                break
            self.counters["Resolve Cycles"] += 1
            output("RESOLVE #%d..." % self.counters["Resolve Cycles"], highlight=True)
            self.matrix.output()
        return len([True for c in self.matrix.cells() if not c.is_exactly()]) == 0

    def switch_guessture_env(self):
        if self.guesstures and self.guesstures[-1]:
            self.counters["Guess Times"] += 1
            self.matrix = self.guesstures[-1][-1].replace_matrix(self.matrix)
            output("GUESS TRY ... %s" % (self.guesstures[-1][-1], ), highlight=True)
            self.summary_guesstures()

    def rollback_guessture_env(self):
        while self.guesstures:
            output("GUESS FAIL ... %s" % (self.guesstures[-1][-1], ), highlight=True)

            self.matrix = self.guesstures[-1].pop(-1).rollback_matrix()
            if len(self.guesstures[-1]) > 0:
                break
            self.guesstures.pop(-1)
        self.summary_guesstures()

    def summit_guessture_env(self):
        output("GUESS SUC ... %s" % (self.guesstures[-1][-1], ), highlight=True)
        self.summary_guesstures()

    def resolve_guess(self):
        for rule in self.guess_rules:
            rule(self)
        output("GUESS NEW ... ", highlight=True)
        self.summary_guesstures()

    def run(self):
        while True:
            if len(self.guesstures):
                self.switch_guessture_env()
            try:
                done = resolver.resolve_until()
            except SudokuException as e:
                output("<{CONFLICT}> : %s" % e.msg)
                if len(self.guesstures):
                    self.rollback_guessture_env()
            else:
                if len(self.guesstures):
                    self.summit_guessture_env()
                if done:
                    break
                resolver.resolve_guess()

    def summary_resolve(self):
        for idx, history in enumerate(self.histories):
            output("<[#%3d Generation]>" % idx)
            history.output()

        output("  ---=== RESULTS ===---  ", highlight=True)
        unresolved_cnt = 0
        self.matrix.output()

        for cell in self.matrix.cells():
            if not cell.is_exactly():
                output(repr(cell))
                unresolved_cnt += 1
        if unresolved_cnt > 0:
            output("UNSOLVED COUNT : %d" % unresolved_cnt, highlight=True)

        output(" ---=== STATICS ===--- ", highlight=True)
        for counter in self.counters.keys():
            output("%15s <[:]> %d" % (counter, self.counters[counter]))

    def summary_guesstures(self):
        output(" --- GUESS STACK --- ", highlight=True)
        for guess_list in self.guesstures:
            output(guess_list)

def rule_sequence_unique(seq):
    if seq.seq_type == Sequence.TIP:
        return False

    modified = False
    output("RULE %9s on [%s] #%d : %s" % ("UNIQUE", seq.seq_type, seq.index, str(seq)), highlight=True)
    have_numbers_list = [c.get_value() for c in seq if c.is_exactly()]
    have_numbers = set(have_numbers_list)
    if len(have_numbers_list) != len(have_numbers):
        raise SudokuException(None, seq, "Confirmed Numbers of sequence have CONFLICTION!")
    for cell in seq:
        if not cell.is_exactly():
            old_options = cell.get_value()
            new_options = old_options - have_numbers
            if len(new_options) == 0:
                raise SudokuException(cell, seq, "NO CHIOCE on the cell!")
            if new_options != old_options:
                modified = True
                cell.set_value(new_options)
                output("(%d, %d) : %s" % (cell.row_index, cell.col_index, cell.get_value()))
                output(" <- %s - %s" % (old_options, have_numbers))
        else:
            pass
    return modified

def rule_sequence_exclude(seq):
    if seq.seq_type == Sequence.TIP:
        return False

    modified = False
    output("RULE %9s on [%s] #%d : %s" % ("EXCLUDE", seq.seq_type, seq.index, str(seq)), highlight=True)
    unexactly_cells = [c for c in seq if not c.is_exactly()]
    for cell in unexactly_cells:
        cell_options = cell.get_value()
        other_same_cells = []
        other_diff_cells = []
        output("TEST >> (%d, %d) %s" % (cell.row_index, cell.col_index, cell_options))
        for other_cell, other_options in seq.superset_cells(cell_options):
            if len(other_options) == 0:
                other_same_cells.append(other_cell)
            else:
                other_diff_cells.append((other_cell, other_options))

        if len(other_same_cells) > 0 and len(other_diff_cells) > 0:
            output("  ==> %s" % (other_same_cells, ))
            for diff_cell, diff_option in other_diff_cells:
                output("  <== %20s -> %s" % (repr(diff_cell), diff_option))

        if len(other_same_cells) == len(cell_options) and len(other_diff_cells) > 0:

            modified = True
            for update_cell, update_option in other_diff_cells:
                    if len(update_option) == 0:
                        raise SudokuException(update_cell, seq, "NO CHIOCE on the cell by other cells excludes!")

                    old_options = update_cell.get_value()
                    update_cell.set_value(update_option)
                    output("(%d, %d) : %20s <- %s - %s" % \
                        (update_cell.row_index, update_cell.col_index, \
                        update_option, old_options, cell_options))
            break
    return modified

def rule_sequence_tip(seq):
    if seq.seq_type != Sequence.TIP:
        return False

    modified = False
    tip_name = lambda seq: seq.matrix.tips_name[seq.index]
    tip_sum = lambda seq: seq.matrix.tips_num[tip_name(seq)]
    output("RULE %9s on [%s] #%s : %3d <- %s" % ("TIPS", seq.seq_type, tip_name(seq), tip_sum(seq), str(seq)), highlight=True)

    unknown_cells = [cell for cell in seq if not cell.is_exactly()]
    known_cells_sum = sum([cell.get_value() for cell in seq if cell.is_exactly()])
    rest_cells_sum = tip_sum(seq) - known_cells_sum
    if rest_cells_sum < 0:
        raise SudokuException(None, seq, "Area sum not match!")

    if len(unknown_cells) > 0:
        if len(unknown_cells) == 1:
            cell = unknown_cells[0]
            output("(%d, %d) %d <- %d - sum(%s)" % (cell.row_index, cell.col_index, rest_cells_sum, tip_sum(seq), str(seq)))
            cell.set_value(rest_cells_sum)
            modified = True
        else:
            cells_options = set()
            for cell in unknown_cells:
                cells_options.update(cell.get_value())
            all_combinations = list(combinations(cells_options, len(unknown_cells)))
            allow_options = set()
            for combination in all_combinations:
                if sum(combination) == rest_cells_sum:
                    allow_options.update(list(combination))
            for cell in unknown_cells:
                old_value = cell.get_value()
                new_value = old_value & allow_options
                if len(new_value) == 0:
                    raise SudokuException(cell, seq, "Area sum not match!")
                cell.set_value(new_value)

    elif rest_cells_sum != 0:
        raise SudokuException(None, seq, "Area sum not match!")

    return modified

def rule_matrix_guessture(slv : Resolver):
    for cell in slv.matrix.cells():
        if not cell.is_exactly():
            slv.guesstures.append(Guessture.make_cell_guesstures(cell))
            break

matrix_size, area_rules_cnt = tuple([int(p) for p in input().split(" ")])
area_rules = {i[0]: int(i[1]) for i in [input().split(" ") for ln in range(0, area_rules_cnt)]}
cell_fmt = lambda x: x[0].isdigit() and (int(x), 0) or (int(x[1:]), x[0])
matrix_data = [[cell_fmt(i) for i in input().split(" ")] for ln in range(0, matrix_size)]
matrix = Matrix([[i[0] for i in ln] for ln in matrix_data], \
                [[i[1] for i in ln] for ln in matrix_data], \
                area_rules)

matrix.output()
for seq in matrix.sequences():
    output("%s : %s" % (seq.seq_type, seq))

resolver = Resolver(matrix)
resolver.sequence_rules.append(rule_sequence_unique)
resolver.sequence_rules.append(rule_sequence_exclude)
resolver.sequence_rules.append(rule_sequence_tip)
resolver.guess_rules.append(rule_matrix_guessture)
resolver.run()
resolver.summary_resolve()

output("SUCCESS RESOLVE THIS SUDOKU GAME!", end=True, highlight=True)
