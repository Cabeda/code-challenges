package advent

// import advent.inputs.One
// import advent.inputs.Two
import advent.inputs.Three


@main def challenge = {
  challenge3_1()
  
}

// def challenge1_2() = {
//   val one = new One()
//   println(one.countTripleDescended(one.inputs))
// }

// def challenge2() = {
//   val two = new Two()
//   val result = two.getFinalPosition(two.inputs)
//   println(two.getTotalCount(result))
// }

// def challenge2_2() = {
//   val two = new Two()
//   val result = two.getFinalPositionWithAim(two.inputs)
//   println(result)
//   println(two.getTotalCount2WithAim(result))
// }

def challenge3_1() = {
  val three = new Three()
  val result = three.getEnergyOutput(three.inputs)

  println(result)

}


