import unittest

from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_nollaa_pienempi_tilavuus_nollaa(self):
        neg_tilavuus_varasto = Varasto(-10)
        self.assertEqual(neg_tilavuus_varasto.tilavuus, 0)

    def test_nollaa_pienempi_saldo_nollaa(self):
        neg_saldo_varasto = Varasto(10, alku_saldo=-10)
        self.assertEqual(neg_saldo_varasto.saldo, 0)

    def test_tilavuus_rajoittaa_saldoa(self):
        varasto = Varasto(tilavuus=10, alku_saldo=20)
        self.assertEqual(varasto.saldo, 10)

    def test_lisaa_negatiivinen_maara(self):
        alku_saldo = self.varasto.saldo
        self.varasto.lisaa_varastoon(-10)
        self.assertEqual(self.varasto.saldo, alku_saldo)

    def test_lisaa_liikaa_tavaraa_varastoon(self):
        tilaa_jaljella = self.varasto.tilavuus - self.varasto.saldo
        self.varasto.lisaa_varastoon(tilaa_jaljella + 1)
        self.assertEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_ota_negatiivinen_maara_tavaraa(self):
        self.assertEqual(self.varasto.ota_varastosta(-10), 0)

    def test_ota_liikaa_tavaraa_varastosta(self):
        saldo = self.varasto.saldo
        self.assertEqual(self.varasto.ota_varastosta(saldo + 1), saldo)

    def test_varasto_merkkijono(self):
        self.assertEqual(
            str(self.varasto),
            f"saldo = {self.varasto.saldo}, vielä tilaa {self.varasto.paljonko_mahtuu()}",
        )
