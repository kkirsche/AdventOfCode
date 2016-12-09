require 'minitest/autorun'

module AdventOfCode
  module Day1
    class TestChallenge < Minitest::Test
      def test_5_blocks_away
        @aoc_day1 = AdventOfCode::Day1::Challenge.new 'test1.txt'
        result = @aoc_day1.run_part_1
        assert_equal 5, result
      end

      def test_2_blocks_away
        @aoc_day1 = AdventOfCode::Day1::Challenge.new 'test2.txt'
        result = @aoc_day1.run_part_1
        assert_equal 2, result
      end

      def test_12_blocks_away
        @aoc_day1 = AdventOfCode::Day1::Challenge.new 'test3.txt'
        result = @aoc_day1.run_part_1
        assert_equal 12, result
      end

      def test_150_blocks_away
        @aoc_day1 = AdventOfCode::Day1::Challenge.new 'test4.txt'
        result = @aoc_day1.run_part_1
        assert_equal 150, result
      end

      def test_first_duplicate_location
        @aoc_day1 = AdventOfCode::Day1::Challenge.new 'test5.txt'
        @aoc_day1.run_part_1
        result = @aoc_day1.run_part_2
        assert_equal 4, result
      end
    end
  end
end
