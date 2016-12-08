require 'set'

module AdventOfCode
  module Day1
    class Position
      attr_accessor :x, :y, :facing

      def initialize(x=0, y=0, facing='N')
        @x = x
        @y = y
        @facing = facing
        @visited = Set.new
        @duplicates = []
      end

      def get_first_duplicate_location
        @duplicates.first
      end

      def turn(direction)
        case @facing
        when 'N'
          turn_from_north direction
        when 'E'
          turn_from_east direction
        when 'S'
          turn_from_south direction
        when 'W'
          turn_from_west direction
        end
      end

      def visited_before
        if @visited.include? [@x, @y]
          @duplicates << (@x.abs + @y.abs)
        end

        @visited << [@x, @y]
      end

      def current_position
        puts "Currently at x,y: #{@x}, #{@y}"
        puts "I am #{total_distance_from_start} blocks from start"
      end

      def walk_north(spaces)
        spaces.times do
          @y += 1
          visited_before
        end
      end

      def walk_south(spaces)
        spaces.times do
          @y -= 1
          visited_before
        end
      end

      def walk_east(spaces)
        spaces.times do
          @x += 1
          visited_before
        end
      end

      def walk_west(spaces)
        spaces.times do
          @x -= 1
          visited_before
        end
      end

      def turn_from_north(direction)
        if direction.left?
          @facing = 'W'
          walk_west direction.spaces
        else
          @facing = 'E'
          walk_east direction.spaces
        end
      end

      def turn_from_east(direction)
        if direction.left?
          @facing = 'N'
          walk_north direction.spaces
        else
          @facing = 'S'
          walk_south direction.spaces
        end
      end

      def turn_from_south(direction)
        if direction.left?
          @facing = 'E'
          walk_east direction.spaces
        else
          @facing = 'W'
          walk_west direction.spaces
        end
      end

      def turn_from_west(direction)
        if direction.left?
          @facing = 'S'
          walk_south direction.spaces
        else
          @facing = 'N'
          walk_north direction.spaces
        end
      end

      def total_distance_from_start
        @x.abs + @y.abs
      end
    end
  end
end
