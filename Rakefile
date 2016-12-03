require "bundler/gem_tasks"
require "rake/testtask"

Rake::TestTask.new(:test) do |t|
  require 'codeclimate-test-reporter'
  CodeClimate::TestReporter.start
  require 'minitest/autorun'
  require "adventOfCode"
  require "adventOfCode/days/01_test"
end

task :default => :test
