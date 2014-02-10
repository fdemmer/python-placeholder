from placeholder import PlaceHolderImage, Size

class TestSize(unittest.TestCase):

    u"""Tests the ``Size`` class.
    """

    def test_width(self):
        s = Size(1, 2)
        self.failUnlessEqual(s.width, 1)

    def test_height(self):
        s = Size(1, 2)
        self.failUnlessEqual(s.height, 2)

    def test_iter(self):
        self.assertEqual(list(Size(1, 2)), [1, 2, ])

    def test_slice0(self):
        Size(1, 2)[0]

    def test_slice1(self):
        Size(1, 2)[1]

    def test_IndexError(self):
        def slice():
            return Size(1, 2)[2]
        self.assertRaises(IndexError, slice)

    def test_min(self):
        self.assertEqual(min(Size(1, 2)), 1)

    def test_max(self):
        self.assertEqual(max(Size(1, 2)), 2)



class TestPlaceHolderImage(unittest.TestCase):

    u"""Tests the ``PlaceHolderImage`` class.
    """

    def test_save(self):
        i = PlaceHolderImage(640, 480)
        i.save()

    def test__txt_img(self):
        # c = Color()
        # i = PlaceHolderImage(640, 480, c.gray)
        # i._txt_img()
        pass
