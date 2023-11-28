package advent.test

import org.scalatest.funsuite._
import advent.One

class OneSpec extends AnyFunSuite {
  test("Returns correct ascended") {
    val inputs = List(1,2)
    val one = new One()
    val result = one.countDescended(inputs)

    assert(result == 1)
  }

  test("Returns correct ascended with equal seq numbers") {
    val inputs = List(1020, 1022, 1022)
    val one = new One()
    val result = one.countDescended(inputs)

    assert(result == 1)
  }

  test("Returns correct with equal seq numbers and ascended") {
    val inputs = List(1024, 1022, 1022)
    val one = new One()
    val result = one.countDescended(inputs)

    assert(result == 0)
  }

  test("Returns correct with increasing sequence") {
    val inputs = List(1020, 1022, 1024, 1026)
    val one = new One()
    val result = one.countDescended(inputs)

    assert(result == 3)
  }
}