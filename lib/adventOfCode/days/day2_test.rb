require 'minitest/autorun'

module AdventOfCode
  module Day2
    class TestChallenge < Minitest::Test
      def test_code_1985
        @aoc_day2 = AdventOfCode::Day2::Challenge.new 'test1.txt'
        result = @aoc_day2.run_part_1
        assert_equal '1985', result
      end
    end
  end
end
