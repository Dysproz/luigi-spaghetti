import luigi
import os
import time


class PreparePlate(luigi.Task):
    path = luigi.Parameter()

    def output(self):
        return luigi.LocalTarget(self.path)

    def run(self):
        time.sleep(5)
        os.makedirs(self.path)


class CookPasta(luigi.Task):
    path = luigi.Parameter()

    def run(self):
        time.sleep(5)
        with open(self.path, 'w') as pasta:
            pasta.write('Cooked Pasta')

    def output(self):
        return luigi.LocalTarget(self.path)

    def requires(self):
        return [PreparePlate(path=os.path.dirname(self.path))]


class CookMeat(luigi.Task):
    path = luigi.Parameter()

    def run(self):
        time.sleep(5)
        with open(self.path, 'w') as meat:
            meat.write('Cooked Meat')

    def output(self):
        return luigi.LocalTarget(self.path)

    def requires(self):
        return [PreparePlate(path=os.path.dirname(self.path))]


class Chop(luigi.Task):
    path = luigi.Parameter()
    ingredient = luigi.Parameter()

    def run(self):
        time.sleep(5)
        with open(self.path, 'w') as ingredient:
            ingredient.write(f'Chopped {self.ingredient}')

    def output(self):
        return luigi.LocalTarget(self.path)

    def requires(self):
        return [PreparePlate(path=os.path.dirname(self.path))]


class MakeTomatoSauce(luigi.Task):
    path = luigi.Parameter()

    def run(self):
        time.sleep(5)
        with open(self.path, 'w') as pasta:
            pasta.write('Tomato Sauce')

    def output(self):
        return luigi.LocalTarget(self.path)

    def requires(self):
        return [PreparePlate(path=os.path.dirname(self.path))]


class MakeStuffing(luigi.Task):
    path = luigi.Parameter()
    id = luigi.Parameter(default='test')

    def requires(self):
        return [Chop(path=f'results/{self.id}/garlic.txt',
                     ingredient='garlic'),
                MakeTomatoSauce(path=f'results/{self.id}/sauce.txt'),
                Chop(path=f'results/{self.id}/onion.txt',
                     ingredient='onion'),
                CookMeat(path=f'results/{self.id}/meat.txt')
                ]

    def run(self):
        time.sleep(5)
        with open(self.input()[0].path, 'r') as garlic_file:
            garlic = garlic_file.read()
        with open(self.input()[1].path, 'r') as sauce_file:
            sauce = sauce_file.read()
        with open(self.input()[2].path, 'r') as onion_file:
            onion = onion_file.read()
        with open(self.input()[3].path, 'r') as meat_file:
            meat = meat_file.read()
        with open(self.path, 'w') as stuffing:
            stuffing.write(f'{garlic} + {sauce} + {onion} + {meat}')

    def output(self):
        return luigi.LocalTarget(self.path)


class MakeSpaghetti(luigi.Task):
    id = luigi.Parameter(default='test')

    def run(self):
        time.sleep(5)
        with open(self.input()[0].path, 'r') as pasta_file:
            pasta = pasta_file.read()
        with open(self.input()[1].path, 'r') as stuffing_file:
            stuffing = stuffing_file.read()
        with open(self.output().path, 'w') as spaghetti:
            spaghetti.write(f'{pasta} + {stuffing}')

    def requires(self):
        return [
            CookPasta(path=f'results/{self.id}/pasta.txt'),
            MakeStuffing(path=f'results/{self.id}/stuffing.txt',
                         id=self.id)
        ]

    def output(self):
        path = f'results/{self.id}/spaghetti.txt'
        return luigi.LocalTarget(path)


if __name__ == '__main__':
    luigi.run()
