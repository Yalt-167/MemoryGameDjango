if __name__ == "__main__":
    # from django.test import TestCase
    from unittest import TestCase, main
    from views import SetupCards


    class TestSetupCards (TestCase):
        def __init__(self, methodName: str = "runTest") -> None:
            super().__init__(methodName)

        def runTest(self) -> None:
            self.assertDrawEnoughCards()
            self.assertDifferentSetOfCards()

        # test wether the function deals enough cards (16 = 2 x 8)
        def assertDrawEnoughCards(self):
            for _ in range(10):
                self.assertEqual(len(SetupCards()), 16)

        # test wether the decks dealt are differents from each other
        def assertDifferentSetOfCards(self):
            def TestOnce(): # returns false if the decks are differents
                deck1 = SetupCards()
                deck2 = SetupCards()
                equalSoFar = True
                idx = 0
                while idx < len(deck1) and equalSoFar:
                    equalSoFar = deck1[idx].name == deck2[idx].name and equalSoFar
                    idx += 1

                return equalSoFar
            
            for _ in range(10):
                self.assertEqual(TestOnce(), False)

    main()

