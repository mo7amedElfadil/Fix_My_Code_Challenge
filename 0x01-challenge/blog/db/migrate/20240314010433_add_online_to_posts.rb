class AddOnlineToPosts < ActiveRecord::Migration[6.0]
  def change
    add_column :posts, :online, :boolean, default: true
  end
end
