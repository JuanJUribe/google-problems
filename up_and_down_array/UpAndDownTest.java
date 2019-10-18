package upanddown;

import org.junit.Assert;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.JUnit4;

@RunWith(JUnit4.class)
public final class UpAndDownTest {
	@Test
	public void testFindMaxIndex_emptyArray() throws Exception {
		int[] emptyArray = new int[0];
		int maxIndex = UpAndDown.findMaxIdx(emptyArray);
		Assert.assertEquals(maxIndex, -1);
	}

	@Test
	public void testFindMaxIndex_oneElement() throws Exception {
		int[] array = { 5 };
		int maxIndex = UpAndDown.findMaxIdx(array);
		Assert.assertEquals(maxIndex, 0);
	}

	@Test
	public void testFindMaxIndex_twoElements_increasing() throws Exception {
		int[] array = { 3, 5 };
		int maxIndex = UpAndDown.findMaxIdx(array);
		Assert.assertEquals(maxIndex, 1);
	}

	@Test
	public void testFindMaxIndex_twoElements_decreasing() throws Exception {
		int[] array = { 5, 2 };
		int maxIndex = UpAndDown.findMaxIdx(array);
		Assert.assertEquals(maxIndex, 0);
	}

	@Test
	public void testFindMaxIndex_threeElements_middle() throws Exception {
		int[] array = { 1, 5, 2 };
		int maxIndex = UpAndDown.findMaxIdx(array);
		Assert.assertEquals(maxIndex, 1);
	}

	@Test
	public void testFindMaxIndex_generalCase_positive() throws Exception {
		int[] array = { 1, 4, 5, 11, 22, 28, 38, 16, 10, 2 };
		int maxIndex = UpAndDown.findMaxIdx(array);
		Assert.assertEquals(maxIndex, 6);
	}

	@Test
	public void testFindMaxIndex_generalCase_negative() throws Exception {
		int[] array = { -20, -17, -5, -4, -2, -1, -3, -7, -19, -25 };
		int maxIndex = UpAndDown.findMaxIdx(array);
		Assert.assertEquals(maxIndex, 5);
	}

	@Test
	public void testFindMaxIndex_generalCase_mixed() throws Exception {
		int[] array = { -20, -17, -5, 4, 8, 9, -3, -7, -19, -25 };
		int maxIndex = UpAndDown.findMaxIdx(array);
		Assert.assertEquals(maxIndex, 5);
	}

	@Test
	public void testFindMaxIndex_sortedIncreasing() throws Exception {
		int[] array = { -20, -17, -5, 4, 8, 9, 19, 25 };
		int maxIndex = UpAndDown.findMaxIdx(array);
		Assert.assertEquals(maxIndex, 7);
	}

	@Test
	public void testFindMaxIndex_sortedDecreasing() throws Exception {
		int[] array = { 3, 0, -1, -2, -5, -8, -27, -134 };
		int maxIndex = UpAndDown.findMaxIdx(array);
		Assert.assertEquals(maxIndex, 0);
	}

	@Test
	public void testFindMaxIndex_extra1() throws Exception {
		int[] array = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0 };
		int maxIndex = UpAndDown.findMaxIdx(array);
		Assert.assertEquals(maxIndex, 9);
	}

	@Test
	public void testFindMaxIndex_extra2() throws Exception {
		int[] array = { 1, 2, 5 };
		int maxIndex = UpAndDown.findMaxIdx(array);
		Assert.assertEquals(maxIndex, 2);
	}

	@Test
	public void testFindMaxIndex_extra3() throws Exception {
		int[] array = { 5, 2, 1 };
		int maxIndex = UpAndDown.findMaxIdx(array);
		Assert.assertEquals(maxIndex, 0);
	}
	@Test
	public void testFindMaxIndex_extra4() throws Exception {
		int[] array = { 5, 3 };
		int maxIndex = UpAndDown.findMaxIdx(array);
		Assert.assertEquals(maxIndex, 0);
	}

}