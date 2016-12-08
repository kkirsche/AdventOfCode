require 'minitest/autorun'

module AdventOfCode
  module Day1
    class TestChallenge < Minitest::Test
      def test_5_blocks_away
        @aoc_day1 = AdventOfCode::Day1::Challenge.new 'test5.txt'
        result = @aoc_day1.run_both_parts
        assert_equal 8, result[:part2]
      end
    end
  end
end
