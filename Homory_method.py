import numpy as np
import math


#  n - маршрутов, m - типов транспорта
#  nt - массив количеств единиц транспорта каждого типа
#  mt - массив количеств мусора, который необходимо вывезти
#  g - массив грузоподъемностей всех типов
#  r - массив расстояний всех маршрутов
#  CpKm - массив расходов в 1км всех типов
#  CpD - массив расходов в день всех типов

def interpret_the_result(basis, b_vect, m, n, opt_func):
    for i in range(len(basis)):
        if basis[i] < m * n:
            type = (basis[i] + 1) // n
            if (basis[i] + 1) % m > 0:
                type += 1
            route = (basis[i] + 1) % n
            if route == 0:
                route = n
            print(
                "Используется " + str(round(b_vect[i])) + " единиц транспорта типа " + str(
                    type) + " на маршруте номер " + str(
                    route))
    print("Расходы: " + str(opt_func))


def fraction_part(number):
    print(number)
    print(math.floor(number))
    print(round(number - math.floor(number), 3))
    fraction = round(number - math.floor(number), 3)
    if fraction < 1e-2:
        fraction = 0
    if fraction == 1:
        fraction = 0
    return fraction


def check_positive(array):
    max = 0
    ind = 0
    for i in range(array.size - 1):
        if array[i] > max:
            max = array[i]
            ind = i
    return max, ind


# def simplex_method(n, m, nt, mt, g, r, CpKm, CpD):
#     # start init
#     simplex_matrix = np.zeros((m + n + 1, n * m + n + m + 1), dtype=np.double)
#     for i in range(m):
#         for j in range(n):
#             simplex_matrix[i][i * n + j] = 1
#         simplex_matrix[i][n * m + i] = 1
#     for i in range(n):
#         for j in range(m):
#             simplex_matrix[m + i][m * j + i] = -g[j]
#         simplex_matrix[m + i][m * n + m + i] = 1
#     for i in range(m):
#         simplex_matrix[i][n * m + n + m] = nt[i]
#     for i in range(n):
#         simplex_matrix[m + i][n * m + n + m] = -mt[i]
#     for i in range(n * m):
#         simplex_matrix[m + n][i] = -1 * (CpD[i % m] + CpKm[i % m] * r[i // m])
#     basis = []
#     for i in range(m + n):
#         basis.append(m * n + i)
#     # end init
#     print(simplex_matrix)
#     print(basis)
#     while True:
#         while True:
#             rows = simplex_matrix.shape[0]
#             columns = simplex_matrix.shape[1]
#             # start dual simplex-method
#             min_b_elem = 0
#             row_ind = 0
#             for i in range(rows):
#                 if simplex_matrix[i][columns - 1] < 0 and simplex_matrix[i][columns - 1] < min_b_elem:
#                     min_b_elem = simplex_matrix[i][columns - 1]
#                     row_ind = i
#             if min_b_elem != 0:
#                 # finding min L / negative matrix[row_ind]
#                 last_min = np.inf
#                 column_ind = 0
#                 for i in range(columns - 1):
#                     print(abs(simplex_matrix[rows - 1][i] / simplex_matrix[row_ind][i]))
#                     if simplex_matrix[row_ind][i] < 0 \
#                             and abs(simplex_matrix[rows - 1][i] / simplex_matrix[row_ind][i]) <= last_min:
#                         last_min = abs(simplex_matrix[rows - 1][i] / simplex_matrix[row_ind][i])
#                         column_ind = i
#                 # changing basis
#                 coef = simplex_matrix[row_ind][column_ind]
#                 for i in range(columns):
#                     simplex_matrix[row_ind][i] /= coef
#                 for i in range(rows):
#                     if i != row_ind:
#                         coef = simplex_matrix[i][column_ind]
#                         for j in range(columns):
#                             simplex_matrix[i][j] -= simplex_matrix[row_ind][j] * coef
#                 basis[row_ind] = column_ind
#             else:
#                 break
#         while True:
#             # start ordinary simplex-method
#             rows = simplex_matrix.shape[0]
#             columns = simplex_matrix.shape[1]
#             max, column_ind = check_positive(simplex_matrix[rows - 1])
#             if max > 0:
#                 min = np.inf
#                 row_ind = 0
#                 for i in range(rows):
#                     coef = simplex_matrix[i][columns - 1] / simplex_matrix[i][column_ind]
#                     if 0 < coef < min:
#                         min = coef
#                         row_ind = i
#                 for i in range(columns):
#                     simplex_matrix[row_ind][i] /= min
#                 for i in range(rows):
#                     if i != row_ind:
#                         coef = simplex_matrix[i][column_ind]
#                         for j in range(n * m + n + m + 1):
#                             simplex_matrix[i][j] -= simplex_matrix[row_ind][j] * coef
#                 basis[row_ind] = column_ind
#             else:
#                 # simplex-method completed, start Homory method
#                 max = 0
#                 num = 0
#                 check_array = []
#                 for i in range(rows - 1):
#                     check = fraction_part(simplex_matrix[i][columns - 1])
#                     check_array.append(check)
#                     print(basis[i])
#                     if check > max and basis[i] < m * n:
#                         max = check
#                         num = i
#                 print("Проверка ", check_array)
#                 print("Максимальная разница ", max)
#                 if max > 0:
#                     new_coefs = []
#                     for i in range(columns):
#                         new_coefs.append(simplex_matrix[num][i] - math.floor(simplex_matrix[num][i]))
#                     simplex_matrix = np.append(simplex_matrix, np.zeros((rows, 1)), axis=1)
#                     columns += 1
#                     simplex_matrix = np.append(simplex_matrix, np.zeros((1, columns)), axis=0)
#                     rows += 1
#                     for i in range(rows):
#                         simplex_matrix[i][columns - 1] = simplex_matrix[i][columns - 2]
#                         simplex_matrix[i][columns - 2] = 0
#                     for i in range(columns):
#                         simplex_matrix[rows - 1][i] = simplex_matrix[rows - 2][i]
#                         simplex_matrix[rows - 2][i] = 0
#                     simplex_matrix[rows - 2][columns - 2] = 1
#                     for i in range(columns - 2):
#                         simplex_matrix[rows - 2][i] = -new_coefs[i]
#                     simplex_matrix[rows - 2][columns - 1] = -new_coefs[columns - 2]
#                     basis.append(columns - 1)
#                     print("Новый базис", basis)
#                     print("Сумма: ", simplex_matrix[rows - 1][columns - 1])
#                     break
#                 else:
#                     # Homory method completed, return result
#                     b_vect = []
#                     for i in range(rows - 1):
#                         b_vect.append(simplex_matrix[i][columns - 1])
#                     opt_func = simplex_matrix[rows - 1][columns - 1]
#                     return basis, b_vect, opt_func


class Homory_method_calculator:
    def __init__(self, routes, transport_types):
        self.upper_bound = 0.99
        self.low_bound = 0.009
        self.routes = routes
        self.transport_types = transport_types
        self.basis = []
        self.characteristics = len(self.routes[0].characteristics)
        self.rows_in_table = len(transport_types) + len(routes) * len(routes[0].characteristics) + 1
        self.columns_in_table = len(transport_types) * len(routes) + len(transport_types) + len(routes) * len(
            routes[0].characteristics) + 1
        self.simplex_table = np.zeros((self.rows_in_table, self.columns_in_table), dtype=np.double)
        self.result = 0
        self.prices_vect = []
        self.basis = []
        self.variants = []
        self.b_vect = []
        self.total_cost = 0
        for i in range(len(self.routes) * len(self.transport_types) + 1, self.columns_in_table):
            self.basis.append(i)
        self.true_variants = len(self.transport_types) * len(self.routes)
        for i in range(1, self.columns_in_table):
            self.variants.append(i)
        for i in range(len(routes)):
            for j in range(len(transport_types)):
                self.prices_vect.append(float(routes[i].length) * float(transport_types[j].cost_per_km) + float(
                    transport_types[j].cost_per_day))
        for i in range(len(self.transport_types)):
            for j in range(len(routes)):
                self.simplex_table[i, j * len(transport_types) + i] = 1
            self.simplex_table[i, len(transport_types) * len(routes) + i] = 1
            self.simplex_table[i, self.columns_in_table - 1] = float(self.transport_types[i].ammount)
        for i in range(len(self.transport_types), self.rows_in_table - 1):
            route = (i - len(self.transport_types)) // self.characteristics
            characteristic = (i - len(self.transport_types)) % self.characteristics
            for j in range(route * len(self.transport_types), (route + 1) * len(self.transport_types)):
                self.simplex_table[i, j] = -1 * float(
                    self.transport_types[j % len(self.transport_types)].characteristics[characteristic])
            self.simplex_table[i, len(self.transport_types) * len(self.routes) + len(self.transport_types) + i - len(
                self.transport_types)] = 1
            self.simplex_table[i, self.columns_in_table - 1] = -1 * float(
                self.routes[route].characteristics[characteristic])
        for i in range(len(self.routes) * len(self.transport_types)):
            self.simplex_table[self.rows_in_table - 1, i] = self.prices_vect[i]
        self.calculate()

    def prepare_for_simplex_method(self):
        while True:
            min_b_elem = 0
            row_ind = -1
            for i in range(self.rows_in_table - 1):
                if self.simplex_table[i, self.columns_in_table - 1] < min_b_elem:
                    min_b_elem = self.simplex_table[i, self.columns_in_table - 1]
                    row_ind = i
            if row_ind == -1:
                self.result = 0
                return
            col_ind = -1
            min_elem = 0
            for i in range(self.columns_in_table - 1):
                if self.simplex_table[row_ind, i] < min_elem:
                    min_elem = self.simplex_table[row_ind, i]
                    col_ind = i
            if col_ind == -1:
                self.result = -1
                return
            elem = self.simplex_table[row_ind, col_ind]
            for i in range(self.columns_in_table):
                self.simplex_table[row_ind, i] /= elem
            for i in range(self.rows_in_table):
                if i != row_ind:
                    elem = self.simplex_table[i, col_ind]
                    for j in range(self.columns_in_table):
                        self.simplex_table[i, j] -= self.simplex_table[row_ind, j] * elem
            self.basis[row_ind] = self.variants[col_ind]

    def simplex_method(self):
        for i in range(self.columns_in_table):
            self.simplex_table[self.rows_in_table - 1, i] *= -1
        while True:
            max_func_elem = 0
            col_ind = 0
            for i in range(self.columns_in_table - 1):
                if self.simplex_table[self.rows_in_table - 1, i] > max_func_elem:
                    max_func_elem = self.simplex_table[self.rows_in_table - 1, i]
                    col_ind = i
            if max_func_elem == 0:
                self.result = 0
                return
            d_i = []
            for i in range(self.rows_in_table - 1):
                if self.simplex_table[i, col_ind] != 0:
                    d_elem = self.simplex_table[i, self.columns_in_table - 1] / self.simplex_table[i, col_ind]
                    if d_elem > 0:
                        d_i.append(d_elem)
                    else:
                        d_i.append(np.inf)
                else:
                    d_i.append(np.inf)
            min_d_elem = np.inf
            row_ind = -1
            for i in range(self.rows_in_table - 1):
                if d_i[i] < min_d_elem:
                    min_d_elem = d_i[i]
                    row_ind = i
            if row_ind == -1:
                self.result = -1
                return
            elem = self.simplex_table[row_ind, col_ind]
            for i in range(self.columns_in_table):
                self.simplex_table[row_ind, i] /= elem
            for i in range(self.rows_in_table):
                if i != row_ind:
                    elem = self.simplex_table[i, col_ind]
                    for j in range(self.columns_in_table):
                        self.simplex_table[i, j] -= self.simplex_table[row_ind, j] * elem
            self.basis[row_ind] = self.variants[col_ind]

    def round_results(self):
        for i in range(self.rows_in_table):
            for j in range(self.columns_in_table):
                if self.simplex_table[i, j] % 1 != 0:
                    if self.simplex_table[i, j] % 1 > self.upper_bound:
                        self.simplex_table[i, j] = self.simplex_table[i, j] // 1 + 1
                    else:
                        if self.simplex_table[i, j] % 1 < self.low_bound:
                            self.simplex_table[i, j] = self.simplex_table[i, j] // 1

    def fract(self, num):
        print(num)
        return round(num - math.floor(num), 3)

    def homory_method(self):
        while True:
            remains = []
            for i in range(self.rows_in_table - 1):
                if self.basis[i] <= self.true_variants:
                    remains.append(self.fract(self.simplex_table[i, self.columns_in_table - 1]))
                else:
                    remains.append(0)
            max_remain = 0
            row_ind = -1
            for i in range(self.rows_in_table - 1):
                if remains[i] > max_remain:
                    max_remain = remains[i]
                    row_ind = i
            if row_ind == -1:
                self.result = 1
                self.b_vect = []
                for i in range(self.rows_in_table - 1):
                    self.b_vect.append(self.simplex_table[i, self.columns_in_table - 1])
                self.total_cost = self.simplex_table[self.rows_in_table - 1, self.columns_in_table - 1]
                return
            print(self.basis)
            print(remains)
            coefs = []
            for i in range(self.columns_in_table):
                coefs.append(-1 * self.fract(self.simplex_table[row_ind, i]))
            print(coefs)
            buffer_table = np.zeros((self.rows_in_table + 1, self.columns_in_table + 1), dtype=np.double)
            for i in range(self.rows_in_table - 1):
                for j in range(self.columns_in_table - 1):
                    buffer_table[i, j] = self.simplex_table[i, j]
            for i in range(self.columns_in_table - 1):
                buffer_table[self.rows_in_table - 1, i] = coefs[i]
            buffer_table[self.rows_in_table - 1, self.columns_in_table - 1] = 1
            buffer_table[self.rows_in_table - 1, self.columns_in_table] = coefs[self.columns_in_table - 1]
            for i in range(self.rows_in_table - 1):
                buffer_table[i, self.columns_in_table] = self.simplex_table[i, self.columns_in_table - 1]
            for i in range(self.columns_in_table - 1):
                buffer_table[self.rows_in_table, i] = self.simplex_table[self.rows_in_table - 1, i]
            buffer_table[self.rows_in_table, self.columns_in_table] = self.simplex_table[self.rows_in_table - 1, self.columns_in_table - 1]
            self.simplex_table = buffer_table
            self.basis.append(len(self.variants) + 1)
            self.variants.append(len(self.variants) + 1)
            self.rows_in_table += 1
            self.columns_in_table += 1
            print(self.simplex_table)
            while True:
                min_b_elem = 0
                row_ind = -1
                for i in range(self.rows_in_table - 1):
                    if self.simplex_table[i, self.columns_in_table - 1] < min_b_elem:
                        min_b_elem = self.simplex_table[i, self.columns_in_table - 1]
                        row_ind = i
                if row_ind == -1:
                    break
                teta_elements = []
                for i in range(self.columns_in_table - 1):
                    if self.simplex_table[row_ind, i] < 0:
                        teta_elements.append(
                            self.simplex_table[self.rows_in_table - 1, i] / self.simplex_table[row_ind, i])
                    else:
                        teta_elements.append(np.inf)
                min_el = np.inf
                col_ind = -1
                for i in range(self.columns_in_table - 1):
                    if teta_elements[i] < min_el:
                        min_el = teta_elements[i]
                        col_ind = i
                if col_ind == -1:
                    self.result = -1
                    return
                elem = self.simplex_table[row_ind, col_ind]
                for i in range(self.columns_in_table):
                    self.simplex_table[row_ind, i] /= elem
                for i in range(self.rows_in_table):
                    if i != row_ind:
                        elem = self.simplex_table[i, col_ind]
                        for j in range(self.columns_in_table):
                            self.simplex_table[i, j] -= self.simplex_table[row_ind, j] * elem
                self.basis[row_ind] = self.variants[col_ind]
            self.round_results()
            print(self.simplex_table)

    def calculate(self):
        self.prepare_for_simplex_method()
        if self.result == -1:
            return
        self.simplex_method()
        if self.result == -1:
            return
        self.round_results()
        if self.result == -1:
            return
        print(self.simplex_table)
        self.homory_method()
        if self.result == 1:
            print(self.simplex_table)
            print(self.simplex_table[self.rows_in_table - 1, self.columns_in_table - 1])
            return
