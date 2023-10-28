package test;

import static org.junit.Assert.*;

import org.junit.jupiter.api.Test;

import sample.Sample_1;

class Sample_1_testTest {

	@Test
	public void test_case_1() {
		String name = "Example";
		String result = Sample_1.hello(name);
		System.out.println(result);
		assertEquals(result, "Hello Example-san !");
	}

}
