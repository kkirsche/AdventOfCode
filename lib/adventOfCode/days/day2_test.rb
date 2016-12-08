require 'minitest/autorun'

module AdventOfCode
  module Day1
    class TestChallenge < Minitest::Test
      def test_5_blocks_away
        @aoc_day1 = AdventOfCode::Day1::Challenge.new 'test5.txt'
        @aoc_day1.run_part_1
        result = @aoc_day1.run_part_2
        assert_equal 8, result
      end
    end
  end
end
