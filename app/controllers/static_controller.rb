class StaticController < ApplicationController
  def home
  end

  def imagetext
  	@content = []
    File.open("myfile.txt", "r").each_line do |line|
      @content.push(line)
    end
  end

  def retweet
  	@content = []
    File.open("myfile.txt", "r").each_line do |line|
      @content.push(line)
    end
  end

  def mentions
  	@content = []
    File.open("myfile.txt", "r").each_line do |line|
      @content.push(line)
    end
  end

  def topten
  	@content = []
    File.open("myfile.txt", "r").each_line do |line|
      @content.push(line)
    end
  end

  def favorite
  	@content = []
    File.open("myfile.txt", "r").each_line do |line|
      @content.push(line)
    end
  end
end
