module AdventOfCode
  module Day1
    class Challenge
      def initialize(filename)
        @position = Position.new
        set_contents filename
      end

      def set_contents(filename)
        # Get instructions
        file = File.open input_path(filename)
        @contents = file.read
      end

      def run
        # Get an array of the directions
        directions_to_hq = @contents.split(', ')

        directions_to_hq.each do |direction|
          direction = Direction.new(direction)
          @position = direction.take_direction @position
        end

        return @position.total_distance_from_start
      end

      @private
      def input_path(filename)
        File.join(File.expand_path('..', File.dirname(File.expand_path(__FILE__))), "inputs/day1/#{filename}")
      end
    end

    class Position
      attr_accessor :x, :y, :facing, :total_blocks

      def initialize(x=0, y=0, facing='N', total_blocks=0)
        @x = x
        @y = y
        @facing = facing
        @total_blocks = total_blocks
      end

      def turn_left(spaces)
        case @facing
        when 'N'
          @facing = 'W'
          walk_west spaces
        when 'E'
          @facing = 'N'
          walk_north spaces
        when 'S'
          @facing = 'E'
          walk_east spaces
        when 'W'
          @facing = 'S'
          walk_south spaces
        end
      end

      def turn_right(spaces)
        case @facing
        when 'N'
          @facing = 'E'
          walk_east spaces
        when 'E'
          @facing = 'S'
          walk_south spaces
        when 'S'
          @facing = 'W'
          walk_west spaces
        when 'W'
          @facing = 'N'
          walk_north spaces
        end
      end

      def current_position
        puts "Currently at x,y: #{@x}, #{@y}"
        puts "I am #{total_distance_from_start} blocks from start"
      end

      def walk_north(spaces)
        @y += spaces
        @total_blocks += spaces
      end

      def walk_south(spaces)
        @y -= spaces
        @total_blocks += spaces
      end

      def walk_east(spaces)
        @x += spaces
        @total_blocks += spaces
      end

      def walk_west(spaces)
        @x -= spaces
        @total_blocks += spaces
      end

      def total_distance_from_start
        @x.abs + @y.abs
      end
    end

    class Direction
      attr_accessor :turn, :spaces
      def initialize(direction)
        # Get the R or L
        @turn = direction[0,1]
        # Get the number of spaces to move
        @spaces = direction[1,2].to_i
      end

      def take_direction(current_position)
        case @turn
        when 'L'
          current_position.turn_left @spaces
        when 'R'
          current_position.turn_right @spaces
        end

        current_position
      end
    end
  end
end
